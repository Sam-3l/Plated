import { Link } from "react-router-dom";

const Home = () => {
    return ( 
        <div className="home">
            <div className="text-4xl font-bold font-serif">Hello y'all</div>
            <br></br>
            <Link to="/recipes"><button type="button" className="bg-blue-300 p-2 rounded me-6">View All Recipes</button></Link>
            <Link to="/recipes/new"><button type="button" className="bg-blue-300 p-2 rounded">Create New Recipe</button></Link>
        </div>
     );
}
 
export default Home;