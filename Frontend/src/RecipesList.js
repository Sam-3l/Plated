import useFetch from "./useFetch";
import { useHistory, Link } from "react-router-dom";

const RecipesList = () => {
    const { data:recipes, isLoading, errors} = useFetch("http://127.0.0.1:8000/api/recipes");
    const history = useHistory();

    const handleClick = () => {
        history.go(-1);
    }

    return ( 
        <div className="recipes-list">
            {isLoading && <div>Loading...</div>}
            {recipes && recipes.map(recipe => (
                <div key={recipe.id}>
                    <Link to={"/recipes/"+recipe.id}><span className='font-bold'>{recipe.name}:</span></Link>
                    <br></br>
                    <span>{recipe.description}</span>
                    <p className='font-serif text-end border-b-2'>{recipe.date_added}</p>
                </div>
            ))}
            {errors && <span className="text-red-500">{errors}</span>}

        <div className="py-10 flex items-center justify-center">
            <button type="button" className="bg-blue-300 p-2 rounded me-7" onClick={handleClick}>GO BACK</button>
            <Link to="/recipes/new"><button type="button" className="bg-blue-300 p-2 rounded">Create Recipe</button></Link>
        </div>
        </div>
     );
}
 
export default RecipesList;