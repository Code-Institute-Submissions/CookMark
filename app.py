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

@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html", difficulties=mongo.db.difficulty.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('index'))

# Create recipe_id with ObjectId and pass it into an edit recipe route
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_difficulties = mongo.db.difficulty.find()
    return render_template('editrecipe.html', recipe = the_recipe, difficulties = all_difficulties)

# Updates the data in mongodb from the edit recipe form
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({"_id": ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'recipe_notes':request.form.get('recipe_notes'),
        'recipe_difficulty':request.form.get('recipe_difficulty')
    })
    return redirect(url_for('index'))

# Deletes the recipe from mongodb when clicking the delete button in index route
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=5000,
    debug=True)