import os
import re
import uuid
from flask import Blueprint, jsonify, request
from pymongo import MongoClient
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
from app import app

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

usuario_teste = {"username": "primeiro@org.com", "password": "123456"}

# Configurar MongoDB
client = MongoClient(os.getenv("MONGO_URI"))
db = client.residencia

# Inicializar Bcrypt
bcrypt = Bcrypt(app)

login_cadastro = Blueprint('login_cadastro', __name__)

def is_valid_email(email):
    # Regex para validar o formato do email 
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$' 
    return re.match(regex, email) is not None

@login_cadastro.route('/cadastro', methods=['POST'])
def cadastro():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    funcao = data.get('funcao')

    # Verifica se o email é válido 
    if not is_valid_email(email): 
        return jsonify({"status": "error", "message": "Email inválido"}), 400 
    
    # Verifica se a senha tem no mínimo 6 caracteres 
    if len(password) < 6: 
        return jsonify({"status": "error", "message": "A senha deve ter no mínimo 6 caracteres"}), 400 
    """
    # Verifica se o usuário já existe
    if db.users.find_one({"username": username}):
        return jsonify({"status": "error", "message": "Usuário já existe"}), 400

    # Criptografar a senha
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Inserir o novo usuário no banco de dados
    db.users.insert_one({
        "username": username,
        "email": email,
        "password": hashed_password,
        "funcao": funcao
    })
    """
    return jsonify({"status": "success", "message": "Usuário cadastrado com sucesso"}), 201

@login_cadastro.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Buscar o usuário no banco de dados
    # user = db.users.find_one({"username": username})

    if username == usuario_teste["username"]:
        if password == usuario_teste["password"]:
            return jsonify({"status": "success", "message": "Sucesso! Usuário logado.", "object": usuario_teste}), 200            
        else:
            return jsonify({"status": "error", "message": "Nome de usuário ou senha incorretos"}), 401
    return jsonify({"status": "error", "message": "Nome de usuário ou senhaaa incorretos"}), 401
    
    """
    # Verifica se o usuário existe e a senha está correta
    if user and bcrypt.check_password_hash(user['password'], password):
        return jsonify({"status": "success", "message": "Login realizado com sucesso"}), 200
    else:
        return jsonify({"status": "error", "message": "Nome de usuário ou senha incorretos"}), 401
    """
