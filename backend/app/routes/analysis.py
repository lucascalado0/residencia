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

routes = Blueprint('analysis', __name__)

def check_hive_connection():
    try:
        response = hive.session.get(f"{os.getenv('THEHIVE_URL')}/api/status")
        return response.status_code == 200
    except Exception as e:
        print(f"Erro ao verificar conexão com TheHive: {e}")
        return False

@routes.route('/analyze_observable', methods=['POST'])
def analyze_observable():
    if not check_hive_connection():
        return jsonify({"status": "error", "message": "TheHive está fora de alcance"}), 503

    data = request.get_json()
    observable = data.get("observable")

    if not observable:
        return jsonify({"status": "error", "message": "Observable não fornecido"}), 400

    try:
        response = hive.analyzer.run(analyzer="MISP_2_1", observable_data=observable, tlp=2)
        if response:
            return jsonify({"status": "success", "analysis": response}), 200
        else:
            return jsonify({"status": "error", "message": response}), 500
    except Exception as e:
        print(f"Erro ao analisar o observable: {e}")
        return jsonify({"status": "error", "message": "Erro ao analisar o observable"}), 500
