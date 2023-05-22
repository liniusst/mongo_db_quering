from pymongo import MongoClient
from pymongo.database import Database


def get_database() -> Database:
    mongodb_host = "localhost"
    mongodb_port = 27017
    database_name = "mongo_quering"
    client = MongoClient(mongodb_host, mongodb_port)
    return client[database_name]
