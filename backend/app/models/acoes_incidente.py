from datetime import datetime
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import pytz

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client['thehive']


class Acoes_Incidente:
    def __init__(self, incidente_id, tipo_acao, descricao, responsavel_id, status, data_execucao=None):
        self.incidente_id = incidente_id
        self.tipo_acao = tipo_acao
        self.descricao = descricao
        self.responsavel_id = responsavel_id
        self.status = status
        self.data_execucao = data_execucao or datetime.now(pytz.timezone('America/Sao_Paulo'))

    @staticmethod
    def from_dict(source):
        return Acoes_Incidente(
            incidente_id=source.get('incidente_id'),
            tipo_acao=source.get('tipo_acao'),
            descricao=source.get('descricao'),
            responsavel_id=source.get('responsavel_id'),
            status=source.get('status'),
            data_execucao=source.get('data_execucao')
        )

    def to_dict(self):
        return {
            'id': str(self._id) if hasattr(self, '_id') else None,
            'incidente_id': self.incidente_id,
            'tipo_acao': self.tipo_acao,
            'descricao': self.descricao,
            'responsavel_id': self.responsavel_id,
            'status': self.status,
            'data_execucao': self.data_execucao
        }

    def save(self):
        if hasattr(self, '_id'):
            db.acoes_incidente.update_one({"_id": self._id}, {"$set": self.to_dict()})
        else:
            result = db.acoes_incidente.insert_one(self.to_dict())
            self._id = result.inserted_id

    @staticmethod
    def find_by_incidente_id(incidente_id):
        data = db.acoes_incidente.find_one({"incidente_id": incidente_id})
        if data:
            acoes_incidente = Acoes_Incidente.from_dict(data)
            acoes_incidente._id = data.get('_id')
            return acoes_incidente
        return None

    @staticmethod
    def find_all():
        return [Acoes_Incidente.from_dict(data) for data in db.acoes_incidente.find()]

    @staticmethod
    def update_acoes_incidente(id, updates):
        db.acoes_incidente.update_one({"_id": id}, {"$set": updates})
