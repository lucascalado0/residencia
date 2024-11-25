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

routes = Blueprint('observables', __name__)

def check_hive_connection():
    try:
        response = hive.session.get(f"{os.getenv('THEHIVE_URL')}/api/status")
        return response.status_code == 200
    except Exception as e:
        print(f"Erro ao verificar conexão com TheHive: {e}")
        return False

@routes.route('/create_observable', methods=['POST'])
def create_observable():
    if not check_hive_connection():
        return jsonify({"status": "error", "message": "TheHive está fora de alcance"}), 503

    data = request.get_json()
    alert_id = data.get("alert_id")
    observables = data.get("observables", [])

    responses = []
    for input_observable in observables:
        response = hive.alert.create_observable(alert_id=alert_id, observable=input_observable)
        responses.append(response.json())
    return jsonify({"status": "success", "observables": responses})

@routes.route('/update_observable', methods=['PUT'])
def update_observable():
    if not check_hive_connection():
        return jsonify({"status": "error", "message": "TheHive está fora de alcance"}), 503

    data = request.get_json()
    alert_id = data.get("alert_id")
    observable_id = data.get("observable_id")
    updated_observable = data.get("updated_observable")

    response = hive.observable.update(observable_id, updated_observable)

    if response.status_code == 200:
        return jsonify({"status": "success", "observable_id": response.json()["_id"]}), 200
    else:
        return jsonify({"status": "error", "message": response.json()}), response.status_code

