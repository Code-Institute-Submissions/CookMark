import os
import ssl
from flask import Flask, render_template, redirect, request, url_for
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

# Error 404 handler, returns the 404.html page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Most app routes are inspired from Code Institutes Mini Project Tutorial
# Home page route, retrieves recipe collection from MongoDB
@app.route('/')
def index():
    return render_template("index.html", recipes=mongo.db.recipes.find())

# Add recipe route, retrieves recipe, difficulty, yield, hour and min collections from MongoDB
@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html", difficulties=mongo.db.difficulty.find(),
     yields=mongo.db.yields.find(), hours=mongo.db.hours.find(), mins=mongo.db.mins.find())

# Inserts the added recipe to MongoDB recipe collection
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('index'))

# View recipe route, retrieves a specific recipe with recipe_id from MongoDB and displays it
@app.route('/get_recipe/<recipe_id>')
def get_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('getrecipe.html', recipe = the_recipe)

# Create recipe_id with ObjectId and pass it into an edit recipe route
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_difficulties = mongo.db.difficulty.find()
    all_yields = mongo.db.yields.find()
    all_hours = mongo.db.hours.find()
    all_mins = mongo.db.mins.find()
    return render_template('editrecipe.html', recipe = the_recipe, difficulties = all_difficulties, yields= all_yields, hours = all_hours, mins = all_mins)

# Updates the data in mongodb from the edit recipe form
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({"_id": ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'recipe_notes':request.form.get('recipe_notes'),
        'recipe_yield':request.form.get('recipe_yield'),
        'recipe_time_hour':request.form.get('recipe_time_hour'),
        'recipe_time_min':request.form.get('recipe_time_min'),
        'recipe_difficulty':request.form.get('recipe_difficulty'),
        'recipe_ingredients':request.form.get('recipe_ingredients'),
        'recipe_directions':request.form.get('recipe_directions'),
        'recipe_url':request.form.get('recipe_url'),
        'recipe_photourl':request.form.get('recipe_photourl')
    })
    return redirect(url_for('index'))

# Deletes the recipe from mongodb when clicking the delete button in index route
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port = int(os.environ.get('PORT', 5000)),
    debug=True)