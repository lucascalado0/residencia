import './App.css'
import './Components/Login.css'
import {BrowserRouter, Route, Routes} from 'react-router-dom'



function App() {

  return (
    <BrowserRouter>
    <Routes>
      <Route path='/' element={<Login/>}/>
      <Route path='/Cadastro' element={<Cadastro_u/>}/>
      <Route path='*' element={<h1>Not Found</h1>}/>
    </Routes>
    </BrowserRouter>

  )

}

export default App
