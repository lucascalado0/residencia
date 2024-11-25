import os
import uuid
from dotenv import load_dotenv
from flask import Blueprint, jsonify, request
from thehive4py import TheHiveApi

load_dotenv()

hive = TheHiveApi(
    url=os.getenv("THEHIVE_URL"),
    username=os.getenv("THEHIVE_USERNAME"),
    password=os.getenv("THEHIVE_PASSWORD")
)

routes = Blueprint('alerts', __name__)

def check_hive_connection():
    try:
        response = hive.session.get(f"{os.getenv('THEHIVE_URL')}/api/status")
        return response.status_code == 200
    except Exception as e:
        print(f"Erro ao verificar conexão com TheHive: {e}")
        return False

@routes.route('/create_alert', methods=['POST'])
def create_alert():
    if not check_hive_connection():
        return jsonify({"status": "error", "message": "TheHive está fora de alcance"}), 503

    data = request.get_json()
    alert_type = data.get("type", "simple")
    source = data.get("source", "teste de alerta via API")
    source_ref = data.get("sourceRef", uuid.uuid4().hex)
    title = data.get("title", "Um teste de alerta via API")
    description = data.get("description", "Criando esse alerta através do backend python")

    input_alert = {
        "type": alert_type,
        "source": source,
        "sourceRef": source_ref,
        "title": title,
        "description": description
    }

    output_alert = hive.alert.create(input_alert)

    if output_alert.status_code == 201:
        return jsonify({"status": "success", "alert_id": output_alert.json()["_id"]}), 201
    else:
        return jsonify({"status": "error", "message": output_alert.json()}), output_alert.status_code

@routes.route('/update_alert', methods=['PUT'])
def update_alert():
    if not check_hive_connection():
        return jsonify({"status": "error", "message": "TheHive está fora de alcance"}), 503

    data = request.get_json()
    alert_id = data.get("alert_id")
    updated_alert = data.get("updated_alert")

    response = hive.alert.update(alert_id, updated_alert)

    if response.status_code == 200:
        return jsonify({"status": "success", "alert_id": response.json()["_id"]}), 200
    else:
        return jsonify({"status": "error", "message": response.json()}), response.status_code

def get_observables_of_alert(alert_id):
    response = hive.alert.find_observables(alert_id)
    if isinstance(response, list): 
        return response 
    else: 
        return []

def get_comments_of_alert(alert_id):
    response = hive.alert.find_comments(alert_id)
    if isinstance(response, list):
        return response
    else:
        return []

@routes.route('/alerts', methods=['GET'])
def get_alerts():
    if not check_hive_connection():
        return jsonify({"status": "error", "message": "TheHive está fora de alcance"}), 503

    alerts = hive.alert.find()

    if isinstance(alerts, list):
        for alert in alerts:
            alert_id = alert["_id"]
            observables = get_observables_of_alert(alert_id)
            comments = get_comments_of_alert(alert_id)
            alert["observables"] = observables
            alert["comments"] = comments

        return jsonify({"status": "success", "alerts": alerts}), 200
    else:
        return jsonify({"status": "error", "message": "Erro ao buscar alertas"}), 500
