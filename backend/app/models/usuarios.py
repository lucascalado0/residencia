from datetime import datetime
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import pytz

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client['thehive']

class Usuario:
    def __init__(self, nome_completo, cpf, chave_passe, email, senha, cargo, is_active=True, is_staff=False, is_superuser=False):
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.chave_passe = chave_passe
        self.email = email
        self.senha = senha
        self.is_active = is_active
        self.is_staff = is_staff
        self.is_superuser = is_superuser
        self.cargo = cargo
        self.created_at = datetime.now(pytz.timezone('America/Sao_Paulo'))
        self.last_login = None

    @staticmethod
    def from_dict(source):
        user = Usuario(
            nome_completo=source.get('nome_completo'),
            cpf=source.get('cpf'),
            chave_passe=source.get('chave_passe'),
            email=source.get('email'),
            senha=source.get('senha'),
            cargo=source.get('cargo'),
            is_active=source.get('is_active', True),
            is_staff=source.get('is_staff', False),
            is_superuser=source.get('is_superuser', False)
        )
        user.created_at = source.get('created_at', datetime.now(pytz.timezone('America/Sao_Paulo')))
        user.last_login = source.get('last_login')
        return user

    def to_dict(self):
        return {
            'nome_completo': self.nome_completo,
            'cpf': self.cpf,
            'chave_passe': self.chave_passe,
            'email': self.email,
            'senha': self.senha,
            'is_active': self.is_active,
            'is_staff': self.is_staff,
            'is_superuser': self.is_superuser,
            'cargo': self.cargo,
            'created_at': self.created_at,
            'last_login': self.last_login
        }

    def save(self):
        db.usuarios.insert_one(self.to_dict())

    @staticmethod
    def find_by_email(email):
        data = db.usuarios.find_one({"email": email})
        if data:
            return Usuario.from_dict(data)
        return None

    @staticmethod
    def update_last_login(email):
        db.usuarios.update_one({"email": email}, {"$set": {"last_login": datetime.now(pytz.timezone('America/Sao_Paulo'))}})
