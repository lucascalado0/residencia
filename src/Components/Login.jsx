import React from 'react'
import { Link } from "react-router-dom"


function Login() {
    return (
        <div className="container">
            <div className='item1'></div>
            <div className='item2'>
                <form action="" method="post" className='formulario'>
                    <label htmlFor="name">Nome de Usuário: </label>
                    <input type="text" placeholder='Insira seu usuario' />
                    <label htmlFor="password">Senha: </label>
                    <input type="password" placeholder='Insira sua senha'/>
                    <button type="button">LOGIN</button>
                </form>
                <Link to='/cadastro_usuario' className='link_cadastro'>Cadastre-se</Link>
            </div>
        </div>
    )

}
export default Login;

