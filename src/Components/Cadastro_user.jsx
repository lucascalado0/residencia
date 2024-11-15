import React from 'react'
import { Link } from "react-router-dom"


function Cadastro () {
    return (
        <div className="container">
           <div className='item1'></div>
            <div className='item2'>
                <form action="" method="post" className='formulario'>
                    <label htmlFor="name">Nome de Usuário: </label>
                    <input type="text" placeholder='Insira seu usuario' required/>
                    <label htmlFor="email">Email: </label>
                    <input type="email" placeholder='Insira seu email' required/>
                    <label htmlFor="password">Senha: </label>
                    <input type="password" placeholder='Insira sua senha'required/>
                    <label htmlFor="funcao">Função: </label>
                    <select name="funcao" id="" className='select_funcao'>
                        <option value="funcao1">Função 1</option>
                        <option value="funcao2">Função 2</option>
                        <option value="funcao3">Função 3</option>
                    </select>
                    <button type="button">CADASTRAR</button>
                </form>
                <Link to='/' className='link_cadastro'>Já possui login?</Link>
            </div>
        </div>
    )

}
export default Cadastro;

