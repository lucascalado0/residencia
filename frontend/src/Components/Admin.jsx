import React from 'react';
import './Admin.css';
import { FaTh, FaRegCopy, FaUser, FaFilter, FaRedo } from 'react-icons/fa';

const Admin = () => {
  return (
    <div className="container">
      <div className="item1-admin">
        <FaTh size={60} style={{ margin: '80px 0 40px 0', color: 'white' }} />
        <FaRegCopy size={60} style={{ margin: '40px 0', color: 'white' }} />
        <FaUser size={60} style={{ margin: '40px 0', color: 'white' }} />
      </div>
      <div className="item2-admin">
        <div className="icons-admin">
          <button className="icon-btn-admin">
            <FaFilter />
          </button>
          <button className="icon-btn-admin">
            <FaRedo />
          </button>
        </div>

        <div className="barra-status">
  <button className="status-btn ativo">
    <strong>Ativos</strong> (50)
  </button>
  <button className="status-btn">
    <strong>Não designado</strong> (8)
  </button>
  <button className="status-btn">
    <strong>Em progresso</strong> (30)
  </button>
  <button className="status-btn">
    <strong>Atrasado</strong> (2)
  </button>
</div>

<hr className="linha-horizontal" />

<h2 className="tasks-ativas-title">Tasks Ativas</h2>

<hr className="linha-horizontal" />
        <div className="barra-pesquisa">
          <input type="text" placeholder="Pesquise por tarefas, nome..." />
        </div>

        <h2 className="detalhes-task">Detalhes da task</h2>

        <div className="comentarios-admin" style={{padding: '0 20px'}}>
  <span className="circulo-admin">LV</span>
  <div>
    <h3 className="comentario-titulo-admin">
      Lorem Ipsum
    </h3>
    <p className="comentario-texto-admin">
      Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quasi aliquid sunt vel porro quibusdam eaque voluptas necessitatibus placeat? Eveniet necessitatibus sit harum tempore molestiae velit perferendis debitis fugit beatae minus.
    </p>
  </div>
</div>
<div className="comentarios-admin" style={{padding: '0 20px'}}>
  <span className="circulo-admin">LV</span>
  <div>
    <h3 className="comentario-titulo-admin">
     Lorem Ipsum
    </h3>
    <p className="comentario-texto-admin">
      Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quasi aliquid sunt vel porro quibusdam eaque voluptas necessitatibus placeat? Eveniet necessitatibus sit harum tempore molestiae velit perferendis debitis fugit beatae minus.
    </p>
  </div>
</div>
<div className="comentarios-admin" style={{padding: '0 20px'}}>
  <span className="circulo-admin">LV</span>
  <div>
    <h3 className="comentario-titulo-admin">
    Lorem Ipsum
    </h3>
    <p className="comentario-texto-admin">
      Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quasi aliquid sunt vel porro quibusdam eaque voluptas necessitatibus placeat? Eveniet necessitatibus sit harum tempore molestiae velit perferendis debitis fugit beatae minus.
    </p>
  </div>
</div>
      </div>
    </div>
  );
};

export default Admin;
