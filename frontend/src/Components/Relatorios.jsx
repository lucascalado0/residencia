import React, { useState, useEffect } from 'react';
import './Relatorios.css';
import { FaFilter, FaRedo, FaCalendarAlt, FaExclamationCircle, FaTags, FaTh, FaRegCopy, FaUser } from 'react-icons/fa';

const Relatorios = () => {
  const [incidentes, setIncidentes] = useState([]);
  const [filtros, setFiltros] = useState({
    data: "",
    tipo: "",
    status: ""
  });
  const [dropdowns, setDropdowns] = useState({
    data: false,
    tipo: false,
    status: false
  });

  useEffect(() => {
    fetch('http://localhost:5000/incidentes')
      .then(response => response.json())
      .then(data => {
        if (data.status === "success") {
          setIncidentes(data.incidentes);
        }
      })
      .catch(error => console.error('Erro ao buscar incidentes:', error));
  }, []);

  const handleFiltroChange = (tipoFiltro, valor) => {
    setFiltros({
      ...filtros,
      [tipoFiltro]: valor
    });
    setDropdowns({
      ...dropdowns,
      [tipoFiltro]: false
    });
  };

  const toggleDropdown = (tipoDropdown) => {
    setDropdowns({
      ...dropdowns,
      [tipoDropdown]: !dropdowns[tipoDropdown]
    });
  };

  const incidentesFiltrados = incidentes.filter(incidente => {
    return (
      (!filtros.data || new Date(incidente.data_criacao).toLocaleDateString() === filtros.data) &&
      (!filtros.tipo || incidente.tipo_incidente === filtros.tipo) &&
      (!filtros.status || incidente.estado === filtros.status)
    );
  });

  return (
    <div className="container">
      <div className="item1-relatorios">
        <a href="dashboard" className="bloco-link"><FaTh size={60} style={{ margin: '80px 0 40px 0', color: 'white' }} /></a>
        <a href="relatorios" className="bloco-link"><FaRegCopy size={60} style={{ margin: '40px 0', color: 'white' }} /></a>
        <a href="admin" className="bloco-link"><FaUser size={60} style={{ margin: '40px 0', color: 'white' }} /></a>
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
          <div className={`dropdown ${dropdowns.data ? 'active' : ''}`}>
            <button className="filtro-btn-relatorios" onClick={() => toggleDropdown('data')}>
              <FaCalendarAlt /> Data
              <span className="barra-relatorios">|</span>
              <span>&#9660;</span>
            </button>
            {dropdowns.data && (
              <div className="dropdown-content">
                <a onClick={() => handleFiltroChange("data", "")}>Todos</a>
                {[...new Set(incidentes.map(incidente => new Date(incidente.data_criacao).toLocaleDateString()))].map((date, index) => (
                  <a key={index} onClick={() => handleFiltroChange("data", date)}>{date}</a>
                ))}
              </div>
            )}
          </div>

          <div className={`dropdown ${dropdowns.tipo ? 'active' : ''}`}>
            <button className="filtro-btn-relatorios" onClick={() => toggleDropdown('tipo')}>
              <FaTags /> Tipo
              <span className="barra-relatorios">|</span>
              <span>&#9660;</span>
            </button>
            {dropdowns.tipo && (
              <div className="dropdown-content">
                <a onClick={() => handleFiltroChange("tipo", "")}>Todos</a>
                {["DNS", "Phishing", "Malware"].map((tipo, index) => (
                  <a key={index} onClick={() => handleFiltroChange("tipo", tipo)}>{tipo}</a>
                ))}
              </div>
            )}
          </div>

          <div className={`dropdown ${dropdowns.status ? 'active' : ''}`}>
            <button className="filtro-btn-relatorios" onClick={() => toggleDropdown('status')}>
              <FaExclamationCircle /> Status
              <span className="barra-relatorios">|</span>
              <span>&#9660;</span>
            </button>
            {dropdowns.status && (
              <div className="dropdown-content">
                <a onClick={() => handleFiltroChange("status", "")}>Todos</a>
                {["Analise", "Concluido", "Em Espera", "Impedidos"].map((status, index) => (
                  <a key={index} onClick={() => handleFiltroChange("status", status)}>{status}</a>
                ))}
              </div>
            )}
          </div>
        </div>

        <table className="tabela-relatorios">
          <thead>
            <tr>
              <th>Tipo do Incidente</th>
              <th>Status</th>
              <th>Data do Incidente</th>
              <th>Ações</th>
            </tr>
          </thead>
          <tbody>
            {incidentesFiltrados.map(incidente => (
              <tr key={incidente.titulo}>
                <td>{incidente.tipo_incidente}</td>
                <td>{incidente.estado}</td>
                <td>{new Date(incidente.data_criacao).toLocaleDateString()}</td>
                <td><button>Ver Detalhes</button></td>
              </tr>
            ))}
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
