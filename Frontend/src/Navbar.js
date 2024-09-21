const Navbar = () => {
    return (  
        <div className="navbar bg-blue-800 px-10 py-4 border-b-2 border-blue-900">
            <ul className="nav-items flex flex-row justify-between">
                <div className="flex flex-row items-center space-x-3 text-white text-base font-sans">
                    <div className="font-bold text-xl cursor-pointer mr-1">PLATED</div>
                    <li><a href="">Home</a></li>
                    <li><a href="">Recipes</a></li>
                    <li><a href="">Orders</a></li>
                    <li><a href="">Ratings</a></li>
                    <li><a href="">Help</a></li>
                </div>
                <div>
                    <span>items to the right</span>
                </div>
            </ul>
        </div>
    );
}
 
export default Navbar;