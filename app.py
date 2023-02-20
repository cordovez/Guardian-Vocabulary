from flask import Flask, redirect, url_for, render_template, request, session, flash
import requests
import json
import pprint
import os

import read_mongo
import mongo_functions.delete_mongo

# from  pymongo import MongoClient
# from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv())

# connection_string = os.environ.get("MONGODB_URI")

# client = MongoClient(connection_string)

# dbs = client.list_database_names()
# guardiandb = client['the-guardian']
# collections = guardiandb.list_collection_names()
# opinions_collection = guardiandb['opinions']

# printer = pprint.PrettyPrinter()


app = Flask(__name__)


@app.route("/")
def home():
    articles = read_mongo.find_all_articles()
    count = read_mongo.count_articles()
    return render_template('index.html', articles=articles, )


@app.route("/articles")
def get_articles():
    data = read_mongo.find_all_articles()
    count = read_mongo.count_articles()
    articles = []
    for article in data:
        article['date'] = article['date'].date()
        articles.append(article)

    return render_template('articles.html', articles=articles, count=count)


@app.route("/vocabulary")
def vocabulary():
    return render_template('vocabulary.html')


if __name__ == "__main__":
    app.run(debug=True)
