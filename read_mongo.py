from  pymongo import MongoClient 
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

connection_string = os.environ.get("MONGODB_URI")

client = MongoClient(connection_string)
guardiandb = client['the-guardian']
opinions_collection = guardiandb['opinions']

def find_all_articles():
    articles = opinions_collection.find()
    return articles

def find_all_journalists():
    journalists = opinions_collection.find()

    for journo in journalists:
        
        print(journo["byline"])

def find_by_name(journo):
    journalist = opinions_collection.find_one({"byline":f'{journo}'})
    
    print(journalist)

def find_article_by_id(article_id):
    from bson.objectid import ObjectId
    _id = ObjectId(article_id)
    article = opinions_collection.find_one(_id)

    print(article)

def count_articles():
    count = opinions_collection.count_documents(filter={})
    return count
