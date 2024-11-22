import React, { useState } from 'react';
import { Link, useNavigate } from "react-router-dom";
import "./mensagem_erro_sucesso.css";

function Cadastro() {
    const [message, setMessage] = useState('');
    const [isError, setIsError] = useState(false); 
    const navigate = useNavigate();

    const handleSubmit = async (event) => {
        event.preventDefault();

        const form = event.target;
        const formData = new FormData(form);
        const username = formData.get("username");
        const email = formData.get("email");
        const password = formData.get("password");
        const funcao = formData.get("funcao");

        const response = await fetch('http://localhost:5000/cadastro', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, email, password, funcao }),
        });

        const data = await response.json();

        if (data.status === 'success') {
            setIsError(false);
            setMessage('Usuário cadastrado com sucesso!');
            setTimeout(() => {
                navigate('/');
            }, 1500);
        } else {
            setMessage(`Erro ao cadastrar usuário: ${data.message}`);
            setIsError(true);
        }
    };

    return (
        <div className="container_cadastro">
            <div className='item1_cadastro'>1</div>
            <div className='item2_cadastro'>
            {message && <div className={`feedback ${isError ? 'error' : ''}`}>{message}</div>}
                <form onSubmit={handleSubmit} className='formulario'>
                    <label htmlFor="name" id='user'>Nome de Usuário: </label>
                    <input type="text" name="username" placeholder='Insira seu usuario' required />
                    <label id='mail' htmlFor="email">Email: </label>
                    <input type="email" name="email" placeholder='Insira seu email' required />
                    <label id='senha' htmlFor="password">Senha: </label>
                    <input type="password" name="password" placeholder='Insira sua senha' required />
                    <label htmlFor="funcao">Função: </label>
                    <select name="funcao" id="function" className='select_funcao'>
                        <option value="funcao1">FUNÇÃO 1</option>
                        <option value="funcao2">FUNÇÃO 2</option>
                        <option value="funcao3">FUNÇÃO 3</option>
                    </select>
                    <button type="submit">CADASTRAR</button>
                </form>
                <Link to='/' className='link_cadastro'>Já possui login?</Link>
            </div>
        </div>
    );
}

export default Cadastro;