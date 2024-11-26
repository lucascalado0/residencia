from flask import Blueprint, jsonify, request
from app.models.incidentes import Incidente

routes = Blueprint('incidentes', __name__)

@routes.route('/incidente', methods=['POST'])
def create_incidente():
    data = request.get_json()
    incidente = Incidente(
        titulo=data.get('titulo'),
        descricao=data.get('descricao'),
        tipo_incidente=data.get('tipo_incidente'),
        estado=data.get('estado'),
        usuario_id=data.get('usuario_id'),
        severidade=data.get('severidade', "Média"),
        fonte_deteccao=data.get('fonte_deteccao')
    )
    incidente.save()
    return jsonify({"status": "success", "message": "Incidente criado com sucesso"}), 201

@routes.route('/incidente', methods=['PUT'])
def update_incidente():
    data = request.get_json()
    titulo = data.get('titulo')
    updates = data.get('updates')
    
    if not titulo or not updates:
        return jsonify({"status": "error", "message": "Titulo e atualizações são necessários"}), 400
    
    Incidente.update_incidente(titulo, updates)
    return jsonify({"status": "success", "message": "Incidente atualizado com sucesso"}), 200

@routes.route('/incidente', methods=['GET'])
def get_incidente():
    titulo = request.args.get('titulo')
    if not titulo:
        return jsonify({"status": "error", "message": "Titulo é necessário"}), 400

    incidente = Incidente.find_by_titulo(titulo)
    if incidente:
        return jsonify({"status": "success", "incidente": incidente.to_dict()}), 200
    else:
        return jsonify({"status": "error", "message": "Incidente não encontrado"}), 404

@routes.route('/incidentes', methods=['GET'])
def get_all_incidentes():
    incidentes = Incidente.find_all()
    incidentes_dict = [incidente.to_dict() for incidente in incidentes]
    return jsonify({"status": "success", "incidentes": incidentes_dict}), 200
