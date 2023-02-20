from  pymongo import MongoClient 
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

connection_string = os.environ.get("MONGODB_URI")

client = MongoClient(connection_string)
guardiandb = client['the-guardian']
opinions_collection = guardiandb['opinions']

def insert_test_doc():
    collection = guardiandb['opinions']

    test_document = {
        "title" : "test document",
        "byline": "JCCorman",
        "type" : "dispose"
    }

    inserted_id = collection.insert_one(test_document).inserted_id
    print(inserted_id)