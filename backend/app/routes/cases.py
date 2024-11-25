import os
from dotenv import load_dotenv
from flask import Blueprint, jsonify, request
from thehive4py import TheHiveApi

load_dotenv()

hive = TheHiveApi(
    url=os.getenv("THEHIVE_URL"),
    username=os.getenv("THEHIVE_USERNAME"),
    password=os.getenv("THEHIVE_PASSWORD")
)

routes = Blueprint('cases', __name__)

def check_hive_connection():
    try:
        response = hive.session.get(f"{os.getenv('THEHIVE_URL')}/api/status")
        return response.status_code == 200
    except Exception as e:
        print(f"Erro ao verificar conexão com TheHive: {e}")
        return False

@routes.route('/create_case', methods=['POST'])
def create_case():
    if not check_hive_connection():
        return jsonify({"status": "error", "message": "TheHive está fora de alcance"}), 503

    data = request.get_json()
    alert_id = data.get("alert_id")
    case_title = data.get("title", "Novo Caso")
    case_description = data.get("description", "Descrição do caso")

    new_case = {
        "title": case_title,
        "description": case_description,
        "tags": ['alerta'],
        "alerts": [alert_id]
    }

    response = hive.case.create(new_case)

    if response.status_code == 201:
        return jsonify({"status": "success", "case_id": response.json()["_id"]}), 201
    else:
        return jsonify({"status": "error", "message": response.json()}), response.status_code

@routes.route('/update_case', methods=['PUT'])
def update_case():
    if not check_hive_connection():
        return jsonify({"status": "error", "message": "TheHive está fora de alcance"}), 503

    data = request.get_json()
    case_id = data.get("case_id")
    updated_case = data.get("updated_case")

    response = hive.case.update(case_id, updated_case)

    if response.status_code == 200:
        return jsonify({"status": "success", "case_id": response.json()["_id"]}), 200
    else:
        return jsonify({"status": "error", "message": response.json()}), response.status_code

@routes.route('/cases', methods=['GET'])
def get_cases():
    if not check_hive_connection():
        return jsonify({"status": "error", "message": "TheHive está fora de alcance"}), 503

    cases = hive.case.find()

    if isinstance(cases, list):
        return jsonify({"status": "success", "cases": cases}), 200
    else:
        return jsonify({"status": "error", "message": "Erro ao buscar casos"}), 500
