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

routes = Blueprint('tasks', __name__)

def check_hive_connection():
    try:
        response = hive.session.get(f"{os.getenv('THEHIVE_URL')}/api/status")
        return response.status_code == 200
    except Exception as e:
        print(f"Erro ao verificar conexão com TheHive: {e}")
        return False

@routes.route('/create_task', methods=['POST'])
def create_task():
    if not check_hive_connection():
        return jsonify({"status": "error", "message": "TheHive está fora de alcance"}), 503

    data = request.get_json()
    case_id = data.get("case_id")
    task_title = data.get("title", "Nova Tarefa")
    task_description = data.get("description", "Descrição da tarefa")

    new_task = {
        "title": task_title,
        "description": task_description
    }

    response = hive.case.create_task(case_id, new_task)

    if response:
        return jsonify({"status": "success", "task_id": response["_id"]}), 201
    else:
        return jsonify({"status": "error", "message": response}), 500

@routes.route('/update_task', methods=['PUT'])
def update_task():
    if not check_hive_connection():
        return jsonify({"status": "error", "message": "TheHive está fora de alcance"}), 503

    data = request.get_json()
    task_id = data.get("task_id")
    updated_task = data.get("updated_task")

    response = hive.task.update(task_id, updated_task)

    if response:
        return jsonify({"status": "success", "task_id": response["_id"]}), 200
    else:
        return jsonify({"status": "error", "message": response}), 500

@routes.route('/tasks', methods=['GET'])
def get_tasks():
    if not check_hive_connection():
        return jsonify({"status": "error", "message": "TheHive está fora de alcance"}), 503

    tasks = hive.task.find()

    if tasks:
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

    if response:
        return jsonify({"status": "success", "task_id": response["_id"]}), 200
    else:
        return jsonify({"status": "error", "message": response}), 500
