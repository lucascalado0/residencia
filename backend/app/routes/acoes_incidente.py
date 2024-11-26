from flask import Blueprint, jsonify, request
from app.models.acoes_incidente import Acoes_Incidente

routes = Blueprint('acoes_incidente', __name__)

@routes.route('/acao', methods=['POST'])
def create_acao():
    data = request.get_json()
    acao = Acoes_Incidente(
        incidente_id=data.get('incidente_id'),
        tipo_acao=data.get('tipo_acao'),
        descricao=data.get('descricao'),
        responsavel_id=data.get('responsavel_id'),
        status=data.get('status')
    )
    acao.save()
    return jsonify({"status": "success", "message": "Ação criada com sucesso"}), 201

@routes.route('/acao/<incidente_id>', methods=['GET'])
def get_acao(incidente_id):
    acao = Acoes_Incidente.find_by_incidente_id(incidente_id)
    if acao:
        return jsonify({"status": "success", "acao": acao.to_dict()}), 200
    else:
        return jsonify({"status": "error", "message": "Ação não encontrada"}), 404

@routes.route('/acoes', methods=['GET'])
def get_all_acoes():
    acoes = Acoes_Incidente.find_all()
    return jsonify({"status": "success", "acoes": [acao.to_dict() for acao in acoes]}), 200

@routes.route('/acao/<id>', methods=['PUT'])
def update_acao(id):
    updates = request.get_json()
    Acoes_Incidente.update_acoes_incidente(id, updates)
    return jsonify({"status": "success", "message": "Ação atualizada com sucesso"}), 200
