from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://nearhanfarhan:{password}@cluster0.8bbckbq.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string)

dbs = client.list_database_names()
recipe_book_db = client.recipe_book
collections = recipe_book_db.list_collection_names()
print(dbs, collections)

def insert_test_doc():
    collection = recipe_book_db.recipes
    test_document = {
        "name": "farhan",
        "message": "hi"
    }
    id = collection.insert_one(test_document).inserted_id
    print(id)

insert_test_doc()