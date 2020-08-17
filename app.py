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
secret_key = os.environ.get('secret_key')

app.config["MONGO_DBNAME"] = MONGO_DBNAME
app.config["MONGO_URI"] = MONGO_URI
app.config["secret_key"] = secret_key
app.secret_key = secret_key

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("index.html", recipes=mongo.db.recipes.find())

@app.route('/get_collections')
def get_collections():
    return render_template("collections.html", collections=mongo.db.collections.find())

@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())

@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html", difficulties=mongo.db.difficulty.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('index'))

# Add st_mtime to the url, overriding the old one and fixing url issue for static files.
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=5000,
    debug=True)