from src import get_config
from pymongo import MongoClient


class Database:
    @staticmethod
    def get_connection(database=None):
        client = MongoClient(get_config("mongo_connect"))
        if database is None:
            return client[get_config("mongo_database")]
        else:
            return client[database]
            
        