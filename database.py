# pylint: disable= missing-docstring
from pymongo import MongoClient
from pymongo.database import Database


# database sukurimas
def get_db(db_name: str) -> Database:
    mongodb_host = "localhost"
    mongodb_port = 27017
    client = MongoClient(mongodb_host, mongodb_port)
    return client[db_name]


# collection sukurimas
def create_collection(db_name: str, collection_name: str) -> Database:
    database = get_db(db_name)
    return database[collection_name]
