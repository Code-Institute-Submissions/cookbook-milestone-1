import os
import datetime
from flask import Flask, flash, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# app.config["IMAGE_UPLOADS"] = 'images'
app.config["MONGO_DBNAME"] = 'Cookbook'
app.config["MONGO_URI"] = 'mongodb+srv://codeinstitute:c0deinstitute@codeinstitute.jmzvl.mongodb.net/cookbook?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/pasta')
def pasta():
    return render_template("pasta.html")


@app.route('/meatandfish')
def meatandfish():
    return render_template("meatandfish.html")


@app.route('/vegetarian')
def vegetarian():
    return render_template("vegetarian.html")


@app.route('/dessert')
def dessert():
    return render_template("dessert.html")


@app.route('/baking')
def baking():
    return render_template("baking.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/recipe')
def recipe():
    return render_template("recipe.html", recipes=mongo.db.recipes.find())


@app.route('/profile')
def profile():
    return render_template("profile.html")


@app.route('/add')
def add():
    return render_template("add.html", recipes=mongo.db.recipes.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    
    x = datetime.datetime.now()
    posted = x.strftime("%d") + " " + x.strftime("%b") + " " + x.strftime("%Y")

    recipes = mongo.db.recipes
    # recipes.insert_one(request.form.to_dict())

    dict1 = request.form.to_dict()
    dict1['posted'] = posted

    recipes.insert_one(dict1)

    if request.files:

        image = request.files["picture"]
        ext = image.filename.rsplit(".", 1)[1]
        path = os.getcwd()
        image_dir = path + "/static/images/" + str(dict1["_id"]) + "." + ext
        #image_dir = path + "/static/images/" + image.filename

        image.save(image_dir)

    # Once that's done, we redirect to recipe.html, so we can view the new recipe in our collection.
    return redirect(url_for('index'))


"""
if __name__ =="__main__":
    app.run(host=os.getenv("IP"),
       port=int(os.getenv("PORT")),
       debug=True)
"""


if __name__ == "__main__":
    app.run(debug=True)
