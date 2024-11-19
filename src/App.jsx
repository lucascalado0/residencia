import './App.css'
import './Components/Login.css'
import Login from './Components/Login'
import Cadastro from './Components/Cadastro_user'
import Admin from './Components/admin_pagina'

import {BrowserRouter, Route, Routes} from 'react-router-dom'



function App() {

  return (
    <BrowserRouter>
    <Routes>
      <Route path='/' element={<Login/>}/>
      <Route path='/cadastro_usuario' element={<Cadastro/>}/>
      <Route path='/admin_page' element={<Admin/>}/>
      <Route path='*' element={<h1>Not Found</h1>}/>
    </Routes>
    </BrowserRouter>

  )

}

export default App
