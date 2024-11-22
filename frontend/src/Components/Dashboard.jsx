import React from 'react';
import './Dashboard.css';
import { FaFilter, FaRedo, FaTh, FaRegCopy, FaUser } from 'react-icons/fa';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const Dashboard = () => {
  
  const combinedData = [
    { name: '', "Análise": 40 },
    { name: '', "Em espera": 93 },
    { name: '', "Concluídos": 72 },
    { name: '', "Não solucionados": 90 },
  ];

  return (
    <div className="container">
      <div className="item1-dashboard">
        <FaTh size={60} style={{ margin: '80px 0 40px 0', color: 'white' }} />
        <FaRegCopy size={60} style={{ margin: '40px 0', color: 'white' }} />
        <FaUser size={60} style={{ margin: '40px 0', color: 'white' }} />
      </div>
      <div className="item2-dashboard">
        <h1 className='h1-dashboard'>DASHBOARD</h1>
        <div className="icons-dashboard">
          <button className="icon-btn-dashboard">
            <FaFilter />
          </button>
          <button className="icon-btn-dashboard">
            <FaRedo />
          </button>
        </div>
        <h2 className='h2-dashboard'>Atividades</h2>

        <div className="blocos-container">
          <div className="bloco bloco-azul">
            <span className="bloco-nome">Incidentes em análise</span>
            <span className="bloco-numero">40</span>
            <a href="#" className="bloco-link">VEJA MAIS</a>
          </div>
          <div className="bloco bloco-verde">
            <span className="bloco-nome">Incidentes concluídos</span>
            <span className="bloco-numero">93</span>
            <a href="#" className="bloco-link">VEJA MAIS</a>
          </div>
          <div className="bloco bloco-laranja">
            <span className="bloco-nome">Incidentes em espera</span>
            <span className="bloco-numero">72</span>
            <a href="#" className="bloco-link">VEJA MAIS</a>
          </div>
          <div className="bloco bloco-vermelho">
            <span className="bloco-nome">Incidentes impedidos</span>
            <span className="bloco-numero">90</span>
            <a href="#" className="bloco-link">VEJA MAIS</a>
          </div>
        </div>
        <h2 className='h2-incidentes'>Incidentes</h2>
        <div className="dashboard-section">
          
          <div className="grafico-container">
            <ResponsiveContainer width="90%" height={550}>
              <BarChart
                width={600}
                height={400}
                data={combinedData}
                margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis ticks={[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]} />
                <Tooltip />
                <Legend />

                <Bar dataKey="Análise" fill="#1F77B4" barSize={50}/>
                <Bar dataKey="Em espera" fill="#FF7F0E" barSize={50}/>
                <Bar dataKey="Concluídos" fill="#2CA02C" barSize={50}/>
                <Bar dataKey="Não solucionados" fill="#D62728" barSize={50}/>
              </BarChart>
            </ResponsiveContainer>
          </div>

          <div className="tabela-container">
            <table className="tabela-dashboard">
              <thead>
                <tr>
                  <td>[tipo do incidente]</td>
                  <td>[status]</td>
                  <td>[data do incidente]</td>
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
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
