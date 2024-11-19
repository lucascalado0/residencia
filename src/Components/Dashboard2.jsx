import React from 'react';
import './Dashboard2.css';
import { FaFilter, FaRegClock } from 'react-icons/fa';

const Dashboard2 = () => {
  return (
    <div className="container">
      <div className='item1'></div>
      <div className='item2'>
        <h1>Detecção de Incidentes</h1>
        <h2>Incidentes recentes</h2>

        <div className="filtros">
          <button className="filtro-btn"><FaFilter /> Filtros</button>
          <button className="filtro-btn"><FaRegClock /> Data</button>
        </div>

        <table className="tabela">
          <thead>
            <tr>
              <th>Data</th>
              <th>Tipo</th>
              <th>Status</th>
              <th>Ações</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>2024-11-18</td>
              <td>Phishing</td>
              <td><span className="status alerta">Alerta</span></td>
              <td><button className="acao-btn">Ver Detalhes</button></td>
            </tr>
            <tr>
              <td>2024-11-17</td>
              <td>Malware</td>
              <td><span className="status resolvido">Resolvido</span></td>
              <td><button className="acao-btn">Ver Detalhes</button></td>
            </tr>
            <tr>
              <td>2024-11-16</td>
              <td>Phishing</td>
              <td><span className="status alerta">Alerta</span></td>
              <td><button className="acao-btn">Ver Detalhes</button></td>
            </tr>
          </tbody>
        </table>

        <div className="paginas">
          <button className="pagina-btn">1</button>
          <button className="pagina-btn">2</button>
          <button className="pagina-btn">3</button>
          <button className="pagina-btn">4</button>
          <button className="pagina-btn">5</button>
        </div>
      </div>
    </div>
  );
};

export default Dashboard2;
