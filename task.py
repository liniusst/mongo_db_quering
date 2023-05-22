# pylint: disable= missing-docstring
import string
import secrets
import random
from pymongo import MongoClient
from pymongo.database import Database

# inputu reiksmes
# database_name = input("Enter database name: ")
# coll_name = input("Enter collection name: ")
field_name, field_type = input("Enter field names and types (vardas,str): ").split(",")
range_min, range_max = input("Enter field ranges (min,max): ").split(",")
num_documents = int(input("Enter number of documents to create: "))

# db pasijungimas iki mongo
client = MongoClient("localhost", 27017)


# database sukurimas
def create_database(db_name: str) -> Database:
    return client[db_name]


# collection sukurimas
def create_collection(db_name: str, collection_name: str) -> Database:
    db = client[db_name]
    return db[collection_name]


# sukuriam random fieldus pagal min ir max reiksmes
def generate_random_data(type_field, min_value, max_value):
    if type_field == "str":
        string = "".join(
            random.choice(string.ascii_lowercase + string.ascii_uppercase)
            for _ in range(min_value, max_value)
        )
        return string
    elif type_field == "int":
        random_int = random.uniform(min_value, max_value)
        return random_int
    elif type_field == "float":
        random_float = round(random.uniform(min_value, max_value), 2)
        return random_float
    else:
        return None


db = client["task_one"]
collection = db["bandymas"]

for _ in range(num_documents):
    document = {}
    document[field_name] = generate_random_data(field_type, range_min, range_max)
    collection.insert_one(document)


# create_database("task_one")
# create_collection("task_one", "bandymas")
generate_random_data(field_type, range_min, range_max)
