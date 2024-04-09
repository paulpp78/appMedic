from pymongo.mongo_client import MongoClient
from config import Config


def get_mongo_client():
    return MongoClient(Config.MONGO_URI)
