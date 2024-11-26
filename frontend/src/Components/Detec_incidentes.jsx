import React from 'react';
import './Detec_incidentes.css';
import { FaTh, FaRegCopy, FaUser, FaFilter, FaRedo, FaCalendarAlt, FaTags, FaExclamationCircle } from 'react-icons/fa';

const DetecIncidentes = () => {
  return (
    <div className="container">
      <div className="item1-detec">
      <a href="dashboard" className="bloco-link"><FaTh size={60} style={{ margin: '80px 0 40px 0', color: 'white' }} /></a>
        <a href="relatorios" className="bloco-link"><FaRegCopy size={60} style={{ margin: '40px 0', color: 'white' }} /></a>
        <a href="admin" className="bloco-link"><FaUser size={60} style={{ margin: '40px 0', color: 'white' }} /></a>
      </div>
      <div className='item2-detec'>
        <h1 className='h1-detec'>Detecção de Incidentes</h1>
        <div className="icons-detec">
          <button className="icon-btn-detec">
            <FaFilter />
          </button>
          <button className="icon-btn-detec">
            <FaRedo />
          </button>
        </div>
        <h2 className='h2-detec'>Incidentes recentes</h2>
        <div className="filtros-detec">
          <button className="filtro-btn-detec">
            <FaCalendarAlt /> Data
            <span className="barra-detec">|</span>
            <span>&#9660;</span>
          </button>

          <button className="filtro-btn-detec">
            <FaTags /> Tipo
            <span className="barra-detec">|</span>
            <span>&#9660;</span>
          </button>

          <button className="filtro-btn-detec">
            <FaExclamationCircle /> Status
            <span className="barra-detec">|</span>
            <span>&#9660;</span>
          </button>
        </div>

        <table className="tabela-detec">
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
              <td><a href="detail_incidentes" className="bloco-link"><button className="acao-btn-detec">Ver Detalhes</button></a></td>
            </tr>
            <tr>
              <td>2024-11-17</td>
              <td>Malware</td>
              <td><span className="status analise">Análise</span></td>
              <td><button className="acao-btn-detec">Ver Detalhes</button></td>
            </tr>
            <tr>
              <td>2024-11-16</td>
              <td>Ransomware</td>
              <td><span className="status não-resolvido">Não Resolvido</span></td>
              <td><button className="acao-btn-detec">Ver Detalhes</button></td>
            </tr>
            <tr>
              <td>2024-11-15</td>
              <td>Man-in-the-Middle</td>
              <td><span className="status resolvido">Resolvido</span></td>
              <td><button className="acao-btn-detec">Ver Detalhes</button></td>
            </tr>
            <tr>
              <td>2024-11-14</td>
              <td>DoS</td>
              <td><span className="status alerta">Alerta</span></td>
              <td><button className="acao-btn-detec">Ver Detalhes</button></td>
            </tr>
            <tr>
              <td>2024-11-13</td>
              <td>Dia zero</td>
              <td><span className="status resolvido">Resolvido</span></td>
              <td><button className="acao-btn-detec">Ver Detalhes</button></td>
            </tr>
          </tbody>
        </table>

        <div className="paginas-detec">
          <button className="pagina-btn-detec">
            &#9664;
          </button>
          <button className="pagina-btn-detec">1</button>
          <button className="pagina-btn-detec">2</button>
          <button className="pagina-btn-detec">3</button>
          <button className="pagina-btn-detec">4</button>
          <button className="pagina-btn-detec">5</button>
          <button className="pagina-btn-detec">
            &#9654;
          </button>
        </div>
      </div>
    </div>
  );
};

export default DetecIncidentes;
