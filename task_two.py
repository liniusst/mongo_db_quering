from typing import List, Dict
from pymongo import MongoClient
from pymongo.collection import Collection

client = MongoClient("localhost", 27017)
db = client["testas_du"]
collection = db["testas_du_coll"]


def filter_documents(
    coll: Collection, field_name: str, equal_vualue: str, not_equal_value: str
) -> List[Dict]:
    query = {field_name: {"$eq": equal_vualue, "$ne": not_equal_value}}
    result = coll.find(query)
    return list(result)


print(filter_documents(collection, "vardas", "agricultor", "antanas"))
