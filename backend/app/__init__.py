from flask import Flask
from flask_cors import CORS
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Inicializar o Bcrypt com o app
    bcrypt.init_app(app)

    from app.routes import alerts, cases, observables, tasks, analysis, login_cadastro, incidentes, evidencias

    app.register_blueprint(alerts.routes)
    app.register_blueprint(cases.routes)
    app.register_blueprint(observables.routes)
    app.register_blueprint(tasks.routes)
    app.register_blueprint(analysis.routes)
    app.register_blueprint(login_cadastro)
    app.register_blueprint(incidentes.routes)
    app.register_blueprint(evidencias.routes)

    @app.route('/') 
    def home(): 
        return "Bem-vindo à Página Inicial do Flask!"    

    return app
