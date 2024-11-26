from datetime import datetime
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import pytz

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client['thehive']


class Evidencia:
    def __init__(self, incidente_id, tipo_evidencia, descricao, arquivo_path, coletado_por, data_coleta=None):
        self.incidente_id = incidente_id
        self.tipo_evidencia = tipo_evidencia
        self.descricao = descricao
        self.arquivo_path = arquivo_path
        self.coletado_por = coletado_por
        self.data_coleta = data_coleta or datetime.now(pytz.timezone('America/Sao_Paulo'))

    @staticmethod
    def from_dict(source):
        return Evidencia(
            incidente_id=source.get('incidente_id'),
            tipo_evidencia=source.get('tipo_evidencia'),
            descricao=source.get('descricao'),
            arquivo_path=source.get('arquivo_path'),
            coletado_por=source.get('coletado_por'),
            data_coleta=source.get('data_coleta')
        )

    def to_dict(self):
        return {
            'id': str(self._id) if hasattr(self, '_id') else None,
            'incidente_id': self.incidente_id,
            'tipo_evidencia': self.tipo_evidencia,
            'descricao': self.descricao,
            'arquivo_path': self.arquivo_path,
            'coletado_por': self.coletado_por,
            'data_coleta': self.data_coleta
        }

    def save(self):
        if hasattr(self, '_id'):
            db.evidencias.update_one({"_id": self._id}, {"$set": self.to_dict()})
        else:
            result = db.evidencias.insert_one(self.to_dict())
            self._id = result.inserted_id

    @staticmethod
    def find_by_incidente_id(incidente_id):
        data = db.evidencias.find_one({"incidente_id": incidente_id})
        if data:
            evidencia = Evidencia.from_dict(data)
            evidencia._id = data.get('_id')
            return evidencia
        return None

    @staticmethod
    def find_all():
        return [Evidencia.from_dict(data) for data in db.evidencias.find()]

    @staticmethod
    def update_evidencia(id, updates):
        db.evidencias.update_one({"_id": id}, {"$set": updates})
