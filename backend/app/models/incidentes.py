from datetime import datetime
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import pytz

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client['thehive']

# TODO
# class Incidentes: