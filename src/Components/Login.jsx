import React from 'react'
import { Link } from "react-router-dom"


function Login() {
    return (
        <div className="container">
            <div className='item1'></div>
            <div className='item2'>
                <form action="" method="get" className='formulario'>
                    <label id='name' htmlFor="name">Nome de Usuário: </label>
                    <input type="text" placeholder='Insira seu usuario' required/>
                    <label htmlFor="password">Senha: </label>
                    <input id='password' type="password" placeholder='Insira sua senha' required/>
                    <button type="submit">LOGIN</button>
                </form>
                <Link to='/cadastro_usuario' className='link_cadastro'>Cadastre-se</Link>
            </div>
        </div>
    )

}
export default Login;

