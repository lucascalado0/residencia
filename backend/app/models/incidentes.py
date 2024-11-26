from datetime import datetime
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import pytz
from bson import ObjectId

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client['thehive']

class Incidente:
    def __init__(self, titulo, descricao, tipo_incidente, estado, data_criacao=None, data_atualizacao=None, usuario_id=None, severidade="Média", fonte_deteccao=None):
        self.titulo = titulo
        self.descricao = descricao
        self.tipo_incidente = tipo_incidente
        self.estado = estado
        self.data_criacao = data_criacao or datetime.now(pytz.timezone('America/Sao_Paulo'))
        self.data_atualizacao = data_atualizacao or datetime.now(pytz.timezone('America/Sao_Paulo'))
        self.usuario_id = usuario_id
        self.severidade = severidade
        self.fonte_deteccao = fonte_deteccao

    @staticmethod
    def from_dict(source):
        return Incidente(
            titulo=source.get('titulo'),
            descricao=source.get('descricao'),
            tipo_incidente=source.get('tipo_incidente'),
            estado=source.get('estado'),
            data_criacao=source.get('data_criacao'),
            data_atualizacao=source.get('data_atualizacao'),
            usuario_id=source.get('usuario_id'),
            severidade=source.get('severidade', "Média"),
            fonte_deteccao=source.get('fonte_deteccao')
        )

    def to_dict(self):
        return {
            'id': str(self._id) if hasattr(self, '_id') else None,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'tipo_incidente': self.tipo_incidente,
            'estado': self.estado,
            'data_criacao': self.data_criacao,
            'data_atualizacao': self.data_atualizacao,
            'usuario_id': self.usuario_id,
            'severidade': self.severidade,
            'fonte_deteccao': self.fonte_deteccao
        }

    def save(self):
        if hasattr(self, '_id'):
            db.incidentes.update_one({"_id": self._id}, {"$set": self.to_dict()})
        else:
            result = db.incidentes.insert_one(self.to_dict())
            self._id = result.inserted_id

    @staticmethod
    def find_by_titulo(titulo):
        data = db.incidentes.find_one({"titulo": titulo})
        if data:
            incidente = Incidente.from_dict(data)
            incidente._id = data.get('_id')
            return incidente
        return None

    @staticmethod
    def find_all():
        return [Incidente.from_dict(data) for data in db.incidentes.find()]

    @staticmethod
    def update_incidente(titulo, updates):
        db.incidentes.update_one({"titulo": titulo}, {"$set": updates})
