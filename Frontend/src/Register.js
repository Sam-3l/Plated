import { useState } from "react";
import { Link, useHistory } from 'react-router-dom';

const Register = () => {
    
    // Form
    const [name, setName] = useState("");
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confpass, setConfPass] = useState("");

    const [error, setError] = useState(null);
    const [level, setLevel] = useState(1);
    const [unameError, setUnameError] = useState(null);

    const history = useHistory();

    const handleUsernameChange = (e) => {
        let uname = e.target.value;
        setUsername(uname);

        const usernameErrorPattern = /[^a-zA-Z0-9_]/;

        fetch("http://127.0.0.1:8000/api/auth/registration/validate-username/?username="+uname)
        .then(res => {
            if (res.ok){
                if (usernameErrorPattern.test(uname)){
                    setUnameError("username can only contain alphanumerics and underscores");
                }
                else{
                    setUnameError(null);
                }
            }
            else{
                throw Error(`username ${uname} is taken. Try again`);
            }
        })
        .catch(err => {
            setUnameError(err.message);
        });
    };

    const handleContinue = (e) => {
        e.preventDefault();

        fetch("http://127.0.0.1:8000/api/auth/registration/validate-email/?email="+email)
        .then(res => {
            if (res.ok){
                setError(null);
                if (!unameError){
                    setLevel(2);
                }
            }
            else{
                throw Error("An account was found with this email.")
            }
        })
        .catch(err => {
            setError(err.message);
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (password !== confpass){
            setError("Passwords do not match");
        }
        else{
            setError(null);
            
            // Submit logic
            
            fetch("http://127.0.0.1:8000/api/auth/registration/", {
                headers : {'Content-Type': 'application/json'},
                method: 'POST',
                body: JSON.stringify({
                    first_name: name,
                    username,
                    email,
                    password1: password,
                    password2: confpass,
                })
            })
            .then(res => {
                if (res.ok){
                    setLevel(3);
                }
                return res.json();
            })
            .then(data => {
                let val = Object.values(data)[0][0];
                throw Error(val);
            })
            .catch(err => {
                setError(err.message);
            });

        };
    };

    return ( 
        <div className="register py-10 sm:px-10 px-3">
            <div className="bg-white xl:mx-96 lg:mx-64 md:mx-40 sm:mx-10 rounded-lg shadow-lg p-6 sm:p-10">
                {level === 1 && (
                    <div>
                        <div className="text-2xl text-center mb-3 font-semibold">
                            Register
                        </div>
                        {error && (
                            <div className="error">
                                { error }
                                &nbsp;
                                <Link to={'/login'} className="underline text-blue-900">Login instead?</Link>
                            </div>
                        )}
                        <form onSubmit={(e) => handleContinue(e)}>
                            <div>
                                <label htmlFor="name">Name</label>
                                <input 
                                    type="text"
                                    id="name"
                                    className="input"
                                    required
                                    placeholder="Input your name"
                                    minLength={3}
                                    value={name}
                                    onChange={(e) => setName(e.target.value)}
                                />
                            </div>
                            <div className="mb-2">
                                <label htmlFor="username">Username</label>
                                <input 
                                    type="text"
                                    id="username" 
                                    className="block p-2 mt-1 mb-0 rounded w-full border-blue-800 border border-opacity-20"
                                    required
                                    placeholder="e.g john_doe"
                                    minLength={5}
                                    value={username}
                                    onChange={(e) => handleUsernameChange(e)}
                                />
                                { username && username.length < 5 && <div className="text-sm text-red-500">username must contain at least 5 characters</div> }
                                { unameError && <div className="text-sm text-red-500">{unameError}</div> }
                                { username && !unameError && username.length >= 5 && <div className="text-sm text-green-600">username {username} is available</div> }
                            </div>
                            <div>
                                <label htmlFor="email">Email</label>
                                <input 
                                    type="email"
                                    id="email" 
                                    className="input"
                                    required
                                    placeholder="johndoe@example.com"
                                    value={email}
                                    onChange={(e) => setEmail(e.target.value)}
                                />
                            </div>
                            <div className="mt-5">
                                <button type="submit" className="btn w-full">Continue</button>
                            </div>
                        </form>
                    </div>
                )}

                {level === 2 && (
                    <div>
                        <div className="text-2xl text-center mb-3 font-semibold">
                            Set Password
                        </div>
                        {error && (
                            <div className="error">
                                { error }
                            </div>
                        )}
                        <form onSubmit={(e) => handleSubmit(e)}>
                            <div>
                                <label htmlFor="password">Password</label>
                                <input 
                                    type="password"
                                    id="password"
                                    className="input"
                                    required
                                    placeholder="Input your password"
                                    minLength={8}
                                    value={password}
                                    onChange={(e) => setPassword(e.target.value)}
                                />
                            </div>
                            <div>
                                <label htmlFor="cpassword">Confirm Password</label>
                                <input 
                                    type="password"
                                    id="cpassword" 
                                    className="input"
                                    required
                                    placeholder="Confirm your password"
                                    minLength={8}
                                    value={confpass}
                                    onChange={(e) => setConfPass(e.target.value)}
                                />
                            </div>
                            <div className="mt-5">
                                <button type="submit" className="btn w-full">Submit</button>
                            </div>
                        </form>
                    </div>
                )}

                { level === 3 && (
                    <div className="email-sent p-3">
                        <div className="flex justify-center mb-3">
                            <svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" width="50" height="50">
                                <path d="m28 6h-24a2 2 0 0 0 -2 2v16a2 2 0 0 0 2 2h24a2 2 0 0 0 2-2v-16a2 2 0 0 0 -2-2zm-2.2 2-9.8 6.78-9.8-6.78zm-21.8 16v-15.09l11.43 7.91a1 1 0 0 0 1.14 0l11.43-7.91v15.09z"/><path d="m0 0h32v32h-32z" fill="none"/>
                            </svg>
                        </div>
                        An email has been sent to <span className="text-blue-900">{email}</span> with a verification link. Check your inbox to verify your email address.

                        <div className="mt-4">
                            <button className="w-full border border-blue-800 border-opacity-30 p-2 rounded-sm hover:bg-blue-50 flex justify-center items-center shadow-md">
                                <span>Open Inbox</span>
                            </button>
                        </div>

                        <div className="mt-3 py-4">Didn't recieve a code?
                        <span className="text-blue-900 ml-1 cursor-pointer hover:underline">resend code</span>
                        </div>
                    </div>
                )}

                { level !== 3 && (
                <div className="foot">

                    <div className="flex mt-3 flex-row justify-center items-center">
                        <hr className="w-full" />
                        <span className="px-3">or</span>
                        <hr className="w-full" />
                    </div>
                    
                    <div className="mt-4">
                        <button className="w-full border border-blue-800 border-opacity-30 text-blue-900 p-2 rounded-sm hover:bg-blue-50 flex justify-center items-center shadow-md">
                            <svg className="w-7 h-7 mr-2" viewBox="-0.5 0 48 48" version="1.1" xmlns="http://www.w3.org/2000/svg">
                                <g id="Icons" stroke="none" strokeWidth="1" fill="none" fillRule="evenodd">
                                    <g id="Color-" transform="translate(-401.000000, -860.000000)">
                                        <g id="Google" transform="translate(401.000000, 860.000000)">
                                            <path d="M9.82727273,24 C9.82727273,22.4757333 10.0804318,21.0144 10.5322727,19.6437333 L2.62345455,13.6042667 C1.08206818,16.7338667 0.213636364,20.2602667 0.213636364,24 C0.213636364,27.7365333 1.081,31.2608 2.62025,34.3882667 L10.5247955,28.3370667 C10.0772273,26.9728 9.82727273,25.5168 9.82727273,24" id="Fill-1" fill="#FBBC05"></path>
                                            <path d="M23.7136364,10.1333333 C27.025,10.1333333 30.0159091,11.3066667 32.3659091,13.2266667 L39.2022727,6.4 C35.0363636,2.77333333 29.6954545,0.533333333 23.7136364,0.533333333 C14.4268636,0.533333333 6.44540909,5.84426667 2.62345455,13.6042667 L10.5322727,19.6437333 C12.3545909,14.112 17.5491591,10.1333333 23.7136364,10.1333333" id="Fill-2" fill="#EB4335"></path>
                                            <path d="M23.7136364,37.8666667 C17.5491591,37.8666667 12.3545909,33.888 10.5322727,28.3562667 L2.62345455,34.3946667 C6.44540909,42.1557333 14.4268636,47.4666667 23.7136364,47.4666667 C29.4455,47.4666667 34.9177955,45.4314667 39.0249545,41.6181333 L31.5177727,35.8144 C29.3995682,37.1488 26.7323182,37.8666667 23.7136364,37.8666667" id="Fill-3" fill="#34A853"></path>
                                            <path d="M46.1454545,24 C46.1454545,22.6133333 45.9318182,21.12 45.6113636,19.7333333 L23.7136364,19.7333333 L23.7136364,28.8 L36.3181818,28.8 C35.6879545,31.8912 33.9724545,34.2677333 31.5177727,35.8144 L39.0249545,41.6181333 C43.3393409,37.6138667 46.1454545,31.6490667 46.1454545,24" id="Fill-4" fill="#4285F4"></path>
                                        </g>
                                    </g>
                                </g>
                            </svg>
                            <span>Sign in with Google</span>
                        </button>
                    </div>

                </div>  )}

            </div>
        </div>
    );
}
 
export default Register;