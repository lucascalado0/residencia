from flask import Blueprint, jsonify, request
from app.models.evidencias import Evidencia

routes = Blueprint('evidencias', __name__)

@routes.route('/evidencia', methods=['POST'])
def create_evidencia():
    data = request.get_json()
    evidencia = Evidencia(
        incidente_id=data.get('incidente_id'),
        tipo_evidencia=data.get('tipo_evidencia'),
        descricao=data.get('descricao'),
        arquivo_path=data.get('arquivo_path'),
        coletado_por=data.get('coletado_por')
    )
    evidencia.save()
    return jsonify({"status": "success", "message": "Evidência criada com sucesso"}), 201

@routes.route('/evidencia/<incidente_id>', methods=['GET'])
def get_evidencia(incidente_id):
    evidencia = Evidencia.find_by_incidente_id(incidente_id)
    if evidencia:
        return jsonify({"status": "success", "evidencia": evidencia.to_dict()}), 200
    else:
        return jsonify({"status": "error", "message": "Evidência não encontrada"}), 404

@routes.route('/evidencias', methods=['GET'])
def get_all_evidencias():
    evidencias = Evidencia.find_all()
    return jsonify({"status": "success", "evidencias": [evidencia.to_dict() for evidencia in evidencias]}), 200

@routes.route('/evidencia/<id>', methods=['PUT'])
def update_evidencia(id):
    updates = request.get_json()
    Evidencia.update_evidencia(id, updates)
    return jsonify({"status": "success", "message": "Evidência atualizada com sucesso"}), 200
