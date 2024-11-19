import React from 'react'
import { Link } from "react-router-dom"


function Cadastro () {
    return (
        <div className="container_cadastro">
            <div className='item1_cadastro'>1</div>
            <div className='item2_cadastro'>
                <form action="" method="get" className='formulario'>
                    <label htmlFor="name" id='user'>Nome de Usuário: </label>
                     <input type="text" placeholder='Insira seu usuario' required/>
                    <label id='mail' htmlFor="email">Email: </label>
                     <input type="email" placeholder='Insira seu email' required/>
                     <label id='senha' htmlFor="password">Senha: </label>
                     <input type="password" placeholder='Insira sua senha'required/>
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