import React from 'react';
import { Link } from "react-router-dom";
import './Cadastro_user.css';  // Importação do arquivo CSS

function Cadastro () {
    return (
        <div className="container">
            <div className='item1-cadastro'></div>
            <div className='item2-cadastro'>
                <form action="" method="get" className='formulario'>
                    <label id='nome' htmlFor="name">Nome de Usuário: </label>
                    <input type="text" placeholder='Insira seu usuario' required/>
                    <label id='mail' htmlFor="email">Email: </label>
                    <input type="email" placeholder='Insira seu email' required/>
                    <label id='senha' htmlFor="password">Senha: </label>
                    <input type="password" placeholder='Insira sua senha'required/>
                    <label id='funcao' htmlFor="funcao">Função: </label>
                    <select name="funcao" id="" className='select_funcao'>
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