import re
from flask import Blueprint, jsonify, request
from dotenv import load_dotenv
from app.models.usuarios import Usuario
from app import bcrypt
import uuid

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

login_cadastro = Blueprint('login_cadastro', __name__)

def is_valid_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

@login_cadastro.route('/cadastro', methods=['POST'])
def cadastro():
    data = request.get_json()
    nome_completo = data.get('nomeCompleto')
    cpf = data.get('cpf')
    chave_passe = uuid.uuid4().hex
    email = data.get('email')
    senha = data.get('password')
    cargo = data.get('funcao')

    if not is_valid_email(email):
        return jsonify({"status": "error", "message": "Email inválido"}), 400

    if len(senha) < 6:
        return jsonify({"status": "error", "message": "A senha deve ter no mínimo 6 caracteres"}), 400

    if Usuario.find_by_email(email):
        return jsonify({"status": "error", "message": "Usuário já existe"}), 400

    hashed_senha = bcrypt.generate_password_hash(senha).decode('utf-8')
    usuario = Usuario(nome_completo, cpf, chave_passe, email, hashed_senha, cargo)
    usuario.save()

    return jsonify({"status": "success", "message": "Usuário cadastrado com sucesso"}), 201

@login_cadastro.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    senha = data.get('password')

    usuario = Usuario.find_by_email(email)
    print(senha)

    if usuario and bcrypt.check_password_hash(usuario.senha, senha):
        Usuario.update_last_login(email)
        return jsonify({"status": "success", "message": "Login realizado com sucesso"}), 200
    else:
        return jsonify({"status": "error", "message": "Email ou senha incorretos"}), 401
