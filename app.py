import os
import ssl
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
  import env

app = Flask(__name__)

MONGO_DBNAME = os.environ.get('MONGO_DBNAME')
MONGO_URI = os.environ.get('MONGO_URI')

app.config["MONGO_DBNAME"] = MONGO_DBNAME
app.config["MONGO_URI"] = MONGO_URI

mongo = PyMongo(app)

@app.route('/')
def index():
  if 'username' in session:
    return 'Welcome' + session['username']

  return render_template('index.html')

@app.route('/get_collections')
def get_collections():
    return render_template("collections.html", collections=mongo.db.collections.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)