# pylint: disable= missing-docstring
# from bson.objectid import ObjectId
from typing import Dict, Any, List
from database import get_db

# Connection to db
db = get_db()
collection = db["users"]


# Simple add user method
def add_user(
    first_name: str, last_name: str, email: str, password: str, age: int
) -> int:
    user_data = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "age": age,
    }
    new_user = collection.insert_one(user_data)
    return new_user.inserted_id


# Get user by user email
def get_user_by_email(email: str) -> Dict[str, Any]:
    all_users = collection.find()
    for user in all_users:
        if email == user["email"]:
            return user


# Filtering using $eq operator (is equal) a == b
def filter_by_equals(field_name: str, value: str) -> List[dict]:
    query = {field_name: {"$eq": value}}
    result = collection.find(query)
    return list(result)


# Filtering using $ne operator (not equal) a != b
def filter_by_not_equals(field_name: str, value: str) -> List[dict]:
    query = {field_name: {"$ne": value}}
    result = collection.find(query)
    return list(result)


# Filtering using $gt operator (greater than) a > b
def filter_by_greater_than(field_name: str, value: int) -> List[dict]:
    query = {field_name: {"$gt": value}}
    result = collection.find(query)
    return list(result)


# Filtering using $lt operator (less than) a < b
def filter_by_less_than(field_name: str, value: int) -> List[dict]:
    query = {field_name: {"$lt": value}}
    result = collection.find(query)
    return list(result)


# add_user("Tom", "Jerry", "tom@pastas.lt", "pa55word", 23)

# Grazina visus dokumentus kur yra pastas pastas@pastas.lt
lygus = filter_by_equals("email", "pastas@pastas.lt")
print(lygus)

# Grazina visus dokumentus kur nera vardo Linas
nelygus = filter_by_not_equals("first_name", "Linas")
print(nelygus)

# Grazina visus vartotojus kuriu amzius didesnis nei 30
didenis = filter_by_greater_than("age", 30)
print(didenis)

# Grazina visus vartotojus kuriu amzius mazesnis nei 50
mazesnis = filter_by_less_than("age", 50)
print(mazesnis)
