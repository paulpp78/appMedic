from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from config import Config

def get_mongo_client():
    return MongoClient(Config.MONGO_URI, server_api=ServerApi('1'))
