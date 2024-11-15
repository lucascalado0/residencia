import React from 'react'
import {Link} from "react-router-dom"



function Login() {
    return (
        <div className="container">
            <form className="login-form">
                <div className="form-group">
                    <label htmlFor="username">Nome de Usuário</label>
                    <input
                        type="text"
                        id="username"
                        name="username"
                        placeholder="Digite seu usuário"
                        required
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="password">Senha</label>
                    <input
                        type="password"
                        id="password"
                        name="password"
                        placeholder="Digite sua senha"
                        required
                    />
                </div>
                <button type="submit">Entrar</button>
            </form>
            <Link to={'/cadastro_usuario'}>Cadastre-se</Link>
        </div>
        
    )

}
export default Login;

