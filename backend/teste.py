import os
from dotenv import load_dotenv

from thehive4py import TheHiveApi
from thehive4py.types.observable import InputObservable
import uuid


load_dotenv()

hive = TheHiveApi(
    url=os.getenv("THEHIVE_URL"), 
    username = os.getenv("THEHIVE_USERNAME"), 
    password = os.getenv("THEHIVE_PASSWORD"))

output_alert = hive.alert.create(
    alert = {
        "type": "simple", 
        "source": "teste de alerta via API",
        "sourceRef": uuid.uuid4().hex, 
        "title": "Um teste de alerta via API", 
        "description": "Criando esse alerta através do backend python"
    }
)

input_observables: list[InputObservable] = [
    {"dataType": "ip", "data": "8.8.8.8"}, 
    {"dataType": "domain", "data": "www.google.com"}, 
]

for input_observable in input_observables:
    hive.alert.create_observable(
        alert_id=output_alert["_id"], observable=input_observable
    )