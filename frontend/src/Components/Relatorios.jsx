import React from 'react';
import './Relatorios.css';
import { FaFilter, FaRedo, FaCalendarAlt, FaExclamationCircle, FaTags, FaTh, FaRegCopy, FaUser } from 'react-icons/fa';

const Relatorios = () => {
  return (
    <div className="container">
      <div className="item1-relatorios">
        <FaTh size={60} style={{ margin: '80px 0 40px 0', color: 'white' }} />
        <FaRegCopy size={60} style={{ margin: '40px 0', color: 'white' }} />
        <FaUser size={60} style={{ margin: '40px 0', color: 'white' }} />
      </div>
      <div className="item2-relatorios">
        <h1 className='h1-relatorios'>Relatórios</h1>
        <div className="icons-relatorios">
          <button className="icon-btn-relatorios">
            <FaFilter />
          </button>
          <button className="icon-btn-relatorios">
            <FaRedo />
          </button>
        </div>
        <h2 className='h2-relatorios'>Incidentes recentes</h2>
        <div className="filtros-relatorios">
          <button className="filtro-btn-relatorios">
            <FaCalendarAlt /> Data
            <span className="barra-relatorios">|</span>
            <span>&#9660;</span>
          </button>

          <button className="filtro-btn-relatorios">
            <FaTags /> Tipo
            <span className="barra-relatorios">|</span>
            <span>&#9660;</span>
          </button>

          <button className="filtro-btn-relatorios">
            <FaExclamationCircle /> Status
            <span className="barra-relatorios">|</span>
            <span>&#9660;</span>
          </button>
        </div>

        <table className="tabela-relatorios">
          <thead>
            <tr>
              <td>[tipo do incidente]</td>
              <td>[status]</td>
              <td>[data do incidente]</td>
              <td>[ações]</td>
            </tr>
            <tr>
              <th></th>
              <th></th>
              <th></th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <th></th>
              <th></th>
              <th></th>
              <th></th>
            </tr>
            <tr>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <th></th>
              <th></th>
              <th></th>
              <th></th>
            </tr>
            <tr>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <th></th>
              <th></th>
              <th></th>
              <th></th>
            </tr>
            <tr>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <th></th>
              <th></th>
              <th></th>
              <th></th>
            </tr>
          </tbody>
        </table>

        <div className="paginas-relatorios">
          <button className="pagina-btn-relatorios">
            &#9664;
          </button>
          <button className="pagina-btn-relatorios">1</button>
          <button className="pagina-btn-relatorios">2</button>
          <button className="pagina-btn-relatorios">3</button>
          <button className="pagina-btn-relatorios">4</button>
          <button className="pagina-btn-relatorios">5</button>
          <button className="pagina-btn-relatorios">
            &#9654;
          </button>
        </div>
      </div>
    </div>
  );
};

export default Relatorios;
