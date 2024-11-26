import React from 'react';
import './Detail_incidentes.css';
import { FaTh, FaRegCopy, FaUser, FaFilter, FaRedo } from 'react-icons/fa';

const DetailIncidentes = () => {
  return (
    <div className="container">
      <div className="item1-detail">
        <a href="dashboard" className="bloco-link"><FaTh size={60} style={{ margin: '80px 0 40px 0', color: 'white' }} /></a>
        <a href="relatorios" className="bloco-link"><FaRegCopy size={60} style={{ margin: '40px 0', color: 'white' }} /></a>
        <a href="admin" className="bloco-link"><FaUser size={60} style={{ margin: '40px 0', color: 'white' }} /></a>
      </div>
      <div className="item2-detail">
        <h1 className='h1-detail'>Detalhes do Incidente</h1>
        <div className="icons-detail">
          <button className="icon-btn-detail">
            <FaFilter />
          </button>
          <button className="icon-btn-detail">
            <FaRedo />
          </button>
        </div>
        <h2 className='h2-detail'>Remetente:</h2>
        <h2 className='h2-detail'>Destinatários:</h2>
        <h2 className='h2-detail'>Link Malicioso:</h2>
        <div className="acoes-detail">
  <h2>Ações:</h2>
  <div className="filtros-detail" style={{ marginBottom: '0' }}>
  <button className="filtro-btn-detail" style={{ marginBottom: '0' }}>Bloquear</button>
  <button className="filtro-btn-detail" style={{ marginBottom: '0' }}>Isolar</button>
  <button className="filtro-btn-detail" style={{ marginBottom: '0' }}>Resolver</button>
</div>
</div>

        <table className="tabela-detail">
          <thead>
            <tr>
              <td>Data da ação</td>
              <td>Responsável</td>
              <td>Ação</td>
              <td>Ações</td>
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
          </tbody>
        </table>

        <div className="paginas-detail">
          <button className="pagina-btn-detail">
            &#9664;
          </button>
          <button className="pagina-btn-detail">1</button>
          <button className="pagina-btn-detail">2</button>
          <button className="pagina-btn-detail">3</button>
          <button className="pagina-btn-detail">4</button>
          <button className="pagina-btn-detail">5</button>
          <button className="pagina-btn-detail">
            &#9654;
          </button>
        </div>
        <h3 className='h3-detail'>Comentários</h3>
<div className="comentarios-detail">
  <span className="circulo-detail">LV</span>
  <div>
    <h3 className="comentario-titulo-detail">
      Lorem Ipsum
    </h3>
    <p className="comentario-texto-detail">
      Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quasi aliquid sunt vel porro quibusdam eaque voluptas necessitatibus placeat? Eveniet necessitatibus sit harum tempore molestiae velit perferendis debitis.
    </p>
  </div>
</div>

      </div>
    </div>
  );
};

export default DetailIncidentes;
