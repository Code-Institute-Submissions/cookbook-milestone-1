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
    tot_doc = mongo.db.recipes.count()
    return render_template("vegetarian.html", recipes=mongo.db.recipes.find(), documents=tot_doc)


@app.route('/dessert')
def dessert():
    return render_template("dessert.html")


@app.route('/baking')
def baking():
    return render_template("baking.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe.html", recipe=the_recipe)


@app.route('/delete_task/<recipe_id>')
def delete_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    oldimg = str(the_recipe['imgfullname'])
    path = os.getcwd()
    oldimgpath = path + "/static/images/" + oldimg
    os.remove(oldimgpath)

    mongo.db.recipes.delete_one({'_id': ObjectId(recipe_id)})
    return redirect(url_for('index'))

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('edit_recipe.html', recipe=the_recipe)


@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes

    recipes.update_one({'_id': ObjectId(recipe_id)}, {"$set":
        {
            "title": request.form.get('title'),
            "category_name": request.form.get('category_name'),
            "ptime": request.form.get('ptime'),
            "ctime": request.form.get('ctime'),
            "serves": request.form.get('serves'),
            "slevel": request.form.get('slevel'),
            "ingredients": request.form.get('ingredients'),
            "method": request.form.get('method')
        }})
    
    if request.files["picture"]:
        the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        oldimg = str(the_recipe['imgfullname'])
        path = os.getcwd()
        oldimgpath = path + "/static/images/" + oldimg
        os.remove(oldimgpath)

        image = request.files["picture"]
        ext = image.filename.rsplit(".", 1)[1]

        image_dir = path + "/static/images/" + str(ObjectId(recipe_id)) + "." + ext
        image.save(image_dir)
        newpicture = str(recipe_id) + "." + ext
        
        recipes.update_one({'_id': ObjectId(recipe_id)}, {"$set":
        {
            "imgfullname": newpicture
        }})

    return redirect(url_for('recipe', recipe_id=recipe_id))



@ app.route('/add')
def add():
    return render_template("add.html", recipes=mongo.db.recipes.find())


@ app.route('/sent')
def sent():
    return render_template("sent.html", recipes=mongo.db.recipes.find())



@ app.route('/insert_recipe', methods=['POST'])
def insert_recipe():

    x=datetime.datetime.now()
    posted=x.strftime("%d") + " " + x.strftime("%b") + " " + x.strftime("%Y")

    recipes=mongo.db.recipes
    # recipes.insert_one(request.form.to_dict())

    dict1=request.form.to_dict()
    dict1['posted']=posted
    dict1['voters']=0
    dict1['votesum']=0
    dict1['imgfullname']=0

    recipes.insert_one(dict1)

    image=request.files["picture"]
    ext=image.filename.rsplit(".", 1)[1]
    path=os.getcwd()
    image_dir=path + "/static/images/" + str(dict1["_id"]) + "." + ext

    image.save(image_dir)

    imgfullname=str(dict1["_id"]) + "." + ext


    myquery={"_id": dict1["_id"]}
    newvalues={"$set": {"imgfullname": imgfullname}}

    recipes.update_one(myquery, newvalues)

    takeid=str(dict1["_id"])

    return redirect(url_for('recipe', recipe_id=takeid))






if __name__ =="__main__":
    app.run(host=os.getenv("IP"),
       port=int(os.getenv("PORT")),
       debug=True)


"""
if __name__ == "__main__":
    app.run(debug=True)
"""