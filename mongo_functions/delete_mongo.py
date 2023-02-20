from pymongo import MongoClient
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

connection_string = os.environ.get("MONGODB_URI")

client = MongoClient(connection_string)
guardiandb = client['the-guardian']
opinions_collection = guardiandb['opinions']


def delete_by_author(name):
    deleted_article = opinions_collection.find_one_and_delete({'byline': name})
    return deleted_article
