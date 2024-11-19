import React from 'react'
import { Link } from "react-router-dom"
import styles from './Cadastro_user.module.css'


function Cadastro () {
    return (
        <div className={styles.container}>
           <div className={styles.item1}></div>
            <div className={styles.item2}>
                <form action="" method="get" className={styles.formulario}>
                    <label htmlFor="name">Nome de Usuário: </label>
                    <input type="text" placeholder='Insira seu usuario' required/>
                    <label htmlFor="email">Email: </label>
                    <input type="email" placeholder='Insira seu email' required/>
                    <label htmlFor="password">Senha: </label>
                    <input type="password" placeholder='Insira sua senha'required/>
                    <label htmlFor="funcao">Função: </label>
                    <select name="funcao" id="" className={styles.select_funcao}>
                        <option value="funcao1">FUNÇÃO 1</option>
                        <option value="funcao2">FUNÇÃO 2</option>
                        <option value="funcao3">FUNÇÃO 3</option>
                    </select>
                    <button type="submit">CADASTRAR</button>
                </form>
                <Link to='/' className={styles.link_cadastro}>Já possui login?</Link>
            </div>
        </div>
    )

}
export default Cadastro;

