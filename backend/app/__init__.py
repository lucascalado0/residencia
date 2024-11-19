from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from app.routes import routes, login_cadastro
app.register_blueprint(routes)
app.register_blueprint(login_cadastro)