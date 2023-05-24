# pylint: disable= missing-docstring
import random
from random_word import RandomWords
from database import get_db


# sukuriam random fieldus pagal min ir max reiksmes
def generate_random(field_type, min_length, max_length):
    if field_type == "str":
        r_word = RandomWords()
        random_word = r_word.get_random_word()
        return random_word
    if field_type == "int":
        random_int = random.randint(int(min_length), int(max_length.get()))
        return random_int
    if field_type == "float":
        random_float = round(random.uniform(min_length.get(), max_length.get()), 2)
        return random_float
    else:
        return None


def generate(
    db_name, collection, need_docs, field_type, field_name, range_min, range_max
):
    client = get_db(db_name.get())
    collection = client[collection.get()]
    need_doc_entry_int = int(need_docs.get())
    for _ in range(need_doc_entry_int):
        document = {}
        document[field_name.get()] = generate_random(
            field_type.get(), range_min.get(), range_max.get()
        )
        collection.insert_one(document)


def update_document(db_name, collection_name, query, update):
    db = get_db(db_name.get())
    collection = db[collection_name]
    result = collection.update_many(query, {"$set": update})
    return result.modified_count


def update_collection(
    db_name, collection, field_type, field_name, range_min, range_max
):
    client = get_db(db_name.get())
    collection = client[collection.get()]
    # need_doc_entry_int = int(need_docs.get())
    for element in collection.find():
        value = generate_random(field_type.get(), range_min.get(), range_max.get())
        element.update_one(
            {}, {"$set": {field_name.get(): value}}, upsert=False, array_filters=None
        )
