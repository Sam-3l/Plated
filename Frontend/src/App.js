import './App.css';
import useFetch from "./useFetch";

function App() {
  const { data:recipes, isLoading, errors} = useFetch("http://127.0.0.1:8000/api/");

  console.log(recipes)

  return (
    <div className="App">
      <div className="content">
        {isLoading && <div>Loading...</div>}
        {recipes && recipes.map(recipe => {
          <div key={recipe.id}>
            <ul>
              <li>{recipe.name}</li>
            </ul>
          </div>
        })}
        {errors && <span>{errors}</span>}
      </div>      
    </div>
  );
}

export default App;
