import './App.css'
import './Components/Login.css'
import Login from './Components/Login'
import Cadastro from './Components/Cadastro_user'
import DetecIncidentes from './Components/Detec_incidentes'
import Admin from './Components/Admin'
import DetailIncidentes from './Components/Detail_incidentes'
import Relatorios from './Components/Relatorios'
import Dashboard from './Components/Dashboard'
import Dashboard2 from './Components/Dashboard2'

import { BrowserRouter, Route, Routes } from 'react-router-dom'

function App() {
  return (
    <BrowserRouter>

      <Routes>
        <Route path='/' element={<Login />} />
        <Route path='/cadastro_usuario' element={<Cadastro />} />
        <Route path='/detec_incidentes' element={<DetecIncidentes />} />
        <Route path='/admin' element={<Admin />} />
        <Route path='/detail_incidentes' element={<DetailIncidentes />} />
        <Route path='/relatorios' element={<Relatorios />} />
        <Route path='/dashboard' element={<Dashboard />} />
        <Route path='/dashboard2' element={<Dashboard2 />} />
        <Route path='*' element={<h1>Not Found</h1>} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
