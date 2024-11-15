import React from 'react'



const Login = () => {
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
            <div>
                <a href="Cadastro_u.jsx">Cadastre-se</a>
            </div>

        </div>





    )

}
export default Login;

