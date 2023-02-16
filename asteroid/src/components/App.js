import Signup from "./signup";
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import Login from "./login";
import Home from "./home";
import Predict from "./predict";
function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/login" element={<Login/>}/>
          <Route path="/" element={<Signup/>}/>
          <Route path="/home" element={<Home/>}/>
          <Route path="/predict" element={<Predict/>}/>
        </Routes>
      </Router>
    </div>
  
  )
}

export default App;
