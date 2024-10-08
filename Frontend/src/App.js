import './App.css';
import RecipesList from './RecipesList';
import Navbar from './Navbar';
import Home from './Home';
import CreateRecipe from './CreateRecipe';
import RecipeDetails from './RecipeDetails';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Register from './Register';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <div className='content bg-slate-100'>
          <Switch>
            <Route exact path="/">
              <Home />
            </Route>
            <Route exact path="/recipes">
              <RecipesList />
            </Route>
            <Route path="/recipes/new">
              <CreateRecipe />
            </Route>
            <Route path="/recipes/:id">
              <RecipeDetails />
            </Route>
            <Route exact path="/register">
              <Register />
            </Route>
          </Switch>
        </div>    
      </div>
    </Router>
  );
}

export default App;
