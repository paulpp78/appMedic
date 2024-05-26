from config import Config
from pymongo.mongo_client import MongoClient


def get_mongo_client():
    return MongoClient(Config.MONGO_URI)
