import { useState } from "react";
import { useHistory } from "react-router-dom";

const CreateRecipe = () => {
    const [name, setName] = useState('');
    const [description, setDescription] = useState('');

    const [status, setStatus] = useState(null);
    const [isLoading, setIsLoading] = useState(false);
    const [errors, setErrors] = useState(null);

    const history = useHistory();

    const handleClick = () => {
        history.go(-1);
    }

    const handleSubmit = (e) => {
        e.preventDefault();

        const data = { name, description };
        fetch("http://127.0.0.1:8000/api/recipes", {
            headers: {"Content-Type": "application/json"},
            method: "POST",
            body: JSON.stringify(data)
        })
        .then((response) => {
            if (!response.ok){
                throw Error("could not fetch data");
            }
        })
        .catch(err => {
            console.log(err.message);
            setErrors(err.message)
        })

        if (!errors){
            history.push("/recipes");
            // Add a flash message of some'n later. Using m the status we get
        }
    }

    return ( 
        <div className="create-recipe">
            <span className="font-bold text-4xl text-blue-950">Create New Recipe</span>
            <form className="p-4" onSubmit={e => handleSubmit(e)}>
                <div>
                    <label htmlFor="name" className="font-semibold text-lg">Input Recipe Name:</label>
                    <p><input type="text"
                            className="p-2 w-96 rounded" 
                            id="name" 
                            value={name} 
                            required
                            onChange={e => setName(e.target.value)} 
                    /></p>
                </div>
                <div>
                    <label htmlFor="description" className="font-semibold text-lg">Describe Your Recipe:</label>
                    <p><textarea type="text"
                        id="description" 
                        className="p-3 h-28 w-96 rounded"
                        value={description}
                        required
                        onChange={e => setDescription(e.target.value)}
                    ></textarea></p>
                </div>
                <button type="submit" className="bg-blue-300 p-2 rounded me-3">Create Recipe</button>
                <button type="button" className="bg-blue-300 p-2 rounded" onClick={handleClick}>Back</button>
            </form>
        </div>
     );
}
 
export default CreateRecipe;