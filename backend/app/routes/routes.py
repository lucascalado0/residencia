from app import app
import os
import uuid
from dotenv import load_dotenv
from flask import Blueprint, Flask, jsonify, request
from thehive4py import TheHiveApi
from thehive4py.types.observable import InputObservable

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurar a API do TheHive
hive = TheHiveApi(
    url=os.getenv("THEHIVE_URL"),
    username=os.getenv("THEHIVE_USERNAME"),
    password=os.getenv("THEHIVE_PASSWORD")
)

routes = Blueprint('routes', __name__)

@app.route('/create_alert', methods=['POST'])
def create_alert():
    data = request.get_json()
    alert_type = data.get("type", "simple")
    source = data.get("source", "teste de alerta via API")
    source_ref = data.get("sourceRef", uuid.uuid4().hex)
    title = data.get("title", "Um teste de alerta via API")
    description = data.get("description", "Criando esse alerta através do backend python")

    # Criar o dicionário do alerta
    input_alert = {
        "type": alert_type,
        "source": source,
        "sourceRef": source_ref,
        "title": title,
        "description": description
    }

    # Enviar o alerta usando a API do TheHive
    output_alert = hive.alert.create(alert=input_alert)

    # Verificar se o alerta foi criado com sucesso
    if output_alert.status_code == 201:
        return jsonify({"status": "success", "alert_id": output_alert.json()["_id"]}), 201
    else:
        return jsonify({"status": "error", "message": output_alert.json()}), output_alert.status_code

@app.route('/create_observable', methods=['POST'])
def create_observable():
    data = request.get_json()
    alert_id = data.get("alert_id")
    observables = data.get("observables", [])

    # Adicionar observáveis ao alerta
    responses = []
    for input_observable in observables:
        response = hive.alert.create_observable(
            alert_id=alert_id, observable=input_observable
        )
        responses.append(response.json())

    return jsonify({"status": "success", "observables": responses})



@app.route('/') 
def home():
    return "Bem-vindo à Página Inicial do Flask!" 