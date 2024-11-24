import os
import uuid
from dotenv import load_dotenv
from flask import Blueprint, Flask, jsonify, request
from thehive4py import TheHiveApi

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurar a API do TheHive
hive = TheHiveApi(
    url=os.getenv("THEHIVE_URL"),
    username=os.getenv("THEHIVE_USERNAME"),
    password=os.getenv("THEHIVE_PASSWORD")
)

app = Flask(__name__)
routes = Blueprint('routes', __name__)

def check_hive_connection():
    try:
        # Tentar fazer uma requisição simples para verificar a conexão
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

    # Criar o dicionário do alerta
    input_alert = {
        "type": alert_type,
        "source": source,
        "sourceRef": source_ref,
        "title": title,
        "description": description
    }

    # Enviar o alerta usando a API do TheHive
    output_alert = hive.alert.create(input_alert)

    # Verificar se o alerta foi criado com sucesso
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

@routes.route('/create_observable', methods=['POST'])
def create_observable():
    if not check_hive_connection():
        return jsonify({"status": "error", "message": "TheHive está fora de alcance"}), 503

    data = request.get_json()
    alert_id = data.get("alert_id")
    observables = data.get("observables", [])

    # Adicionar observáveis ao alerta
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

    # Obter todos os alertas
    alerts = hive.alert.find()

    # Verificar se a solicitação retornou resultados
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

@routes.route('/create_case', methods=['POST'])
def create_case():
    if not check_hive_connection():
        return jsonify({"status": "error", "message": "TheHive está fora de alcance"}), 503

    data = request.get_json()
    alert_id = data.get("alert_id")
    case_title = data.get("title", "Novo Caso")
    case_description = data.get("description", "Descrição do caso")
    
    # alert_id = "12304"
    # case_title = "Case criado por API"
    # case_description = "Esse Case foi criado via API"

    # Criar um novo caso
    new_case = {
        "title": case_title,
        "description": case_description,
        "tags": ['alerta'],
        "alerts": [alert_id]  # Adicionar alerta ao caso
    }

    response = hive.case.create(new_case)

    # Verificar se o caso foi criado com sucesso
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

    # Obter todos os casos
    cases = hive.case.find()

    # Verificar se a solicitação retornou resultados
    if isinstance(cases, list):
        return jsonify({"status": "success", "cases": cases}), 200
    else:
        return jsonify({"status": "error", "message": "Erro ao buscar casos"}), 500

@routes.route('/analyze_observable', methods=['POST'])
def analyze_observable():
    if not check_hive_connection():
        return jsonify({"status": "error", "message": "TheHive está fora de alcance"}), 503

    data = request.get_json()
    observable = data.get("observable")

    if not observable:
        return jsonify({"status": "error", "message": "Observable não fornecido"}), 400

    # Usar o observable para ser analisado pelo analyzer MISP_2_1
    try:
        response = hive.analyzer.run(analyzer="MISP_2_1", observable_data=observable, tlp=2)
        if response.status_code == 200:
            return jsonify({"status": "success", "analysis": response.json()}), 200
        else:
            return jsonify({"status": "error", "message": response.json()}), response.status_code
    except Exception as e:
        print(f"Erro ao analisar o observable: {e}")
        return jsonify({"status": "error", "message": "Erro ao analisar o observable"}), 500

@routes.route('/create_task', methods=['POST'])
def create_task():
    if not check_hive_connection():
        return jsonify({"status": "error", "message": "TheHive está fora de alcance"}), 503

    data = request.get_json()
    case_id = data.get("case_id")
    task_title = data.get("title", "Nova Tarefa")
    task_description = data.get("description", "Descrição da tarefa")

    # Criar uma nova tarefa
    new_task = {
        "title": task_title,
        "description": task_description
    }

    response = hive.case.create_task(case_id, new_task)

    # Verificar se a tarefa foi criada com sucesso
    if response.status_code == 201:
        return jsonify({"status": "success", "task_id": response.json()["_id"]}), 201
    else:
        return jsonify({"status": "error", "message": response.json()}), response.status_code

@routes.route('/update_task', methods=['PUT'])
def update_task():
    if not check_hive_connection():
        return jsonify({"status": "error", "message": "TheHive está fora de alcance"}), 503

    data = request.get_json()
    task_id = data.get("task_id")
    updated_task = data.get("updated_task")

    response = hive.task.update(task_id, updated_task)

    if response.status_code == 200:
        return jsonify({"status": "success", "task_id": response.json()["_id"]}), 200
    else:
        return jsonify({"status": "error", "message": response.json()}), response.status_code

@routes.route('/tasks', methods=['GET'])
def get_tasks():
    if not check_hive_connection():
        return jsonify({"status": "error", "message": "TheHive está fora de alcance"}), 503

    # Obter todas as tarefas
    tasks = hive.task.find()

    # Verificar se a solicitação retornou resultados
    if isinstance(tasks, list):
        return jsonify({"status": "success", "tasks": tasks}), 200
    else:
        return jsonify({"status": "error", "message": "Erro ao buscar tarefas"}), 500


@routes.route('/update_task_status', methods=['PUT'])
def update_task_status():
    if not check_hive_connection():
        return jsonify({"status": "error", "message": "TheHive está fora de alcance"}), 503

    data = request.get_json()
    task_id = data.get("task_id")
    status = data.get("status")

    if status not in ["Done", "Required"]:
        return jsonify({"status": "error", "message": "Status inválido"}), 400

    updated_task = {
        "status": status
    }

    response = hive.task.update(task_id, updated_task)

    if response.status_code == 200:
        return jsonify({"status": "success", "task_id": response.json()["_id"]}), 200
    else:
        return jsonify({"status": "error", "message": response.json()}), response.status_code

@routes.route('/')
def home():
    return "Bem-vindo à Página Inicial do Flask!"

# Registrar o blueprint
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True)
