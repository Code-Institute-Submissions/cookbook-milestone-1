import os
import datetime
from flask import Flask, flash, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId



app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'Cookbook'
app.config["MONGO_URI"] = 'mongodb+srv://codeinstitute:c0deinstitute@codeinstitute.jmzvl.mongodb.net/cookbook?retryWrites=true&w=majority'

mongo = PyMongo(app)



# MENU LINKS - Home - Pasta - Meat&Fish - Vegetarian - Dessert - Baking - Contact

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/pasta')
def pasta():
    query = {"category_name": "Pasta"}
    return render_template("pasta.html", recipes = mongo.db.recipes.find(query))


@app.route('/meatandfish')
def meatandfish():
    query = {"category_name": "Meat&Fish"}
    return render_template("meatandfish.html", recipes = mongo.db.recipes.find(query))


@app.route('/vegetarian')
def vegetarian():
    query = {"category_name": "Vegetarian"}
    return render_template("vegetarian.html", recipes = mongo.db.recipes.find(query))


@app.route('/dessert')
def dessert():
    query = {"category_name": "Dessert"}
    return render_template("dessert.html", recipes = mongo.db.recipes.find(query))


@app.route('/baking')
def baking():
    query = {"category_name": "Baking"}
    return render_template("baking.html", recipes = mongo.db.recipes.find(query))


@app.route('/contact')
def contact():
    return render_template("contact.html")




# CREATE - READ - UPDATE - DELETE

# CREATE
@app.route('/add')
def add():
    return render_template("add.html", recipes = mongo.db.recipes.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    # date
    x = datetime.datetime.now()
    posted = x.strftime("%d") + " " + x.strftime("%b") + " " + x.strftime("%Y")

    recipes = mongo.db.recipes
    dict1 = request.form.to_dict()
    
    # further variables: date - rate - image name
    dict1['posted'] = posted
    dict1['voters'] = 0
    dict1['votesum'] = 0
    dict1['imgfullname'] = 0

    recipes.insert_one(dict1)

    # saving the image in the image folder and naming by _id i.e. 5f034b69b91c57308938cf82.jpg
    image = request.files["picture"]
    ext = image.filename.rsplit(".", 1)[1]
    path = os.getcwd()
    image_dir = path + "/static/images/" + str(dict1["_id"]) + "." + ext
    image.save(image_dir)

    # saving the image name in the database
    imgfullname = str(dict1["_id"]) + "." + ext
    myquery = {"_id": dict1["_id"]}
    newvalues = {"$set": {"imgfullname": imgfullname}}
    recipes.update_one(myquery, newvalues)

    takeid = str(dict1["_id"])

    return redirect(url_for('recipe', recipe_id = takeid))


# READ - RECIPE PAGE
@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe.html", recipe = the_recipe)


#UPDATE
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('edit_recipe.html', recipe = the_recipe)


@app.route('/update_recipe/<recipe_id>', methods = ['POST'])
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
    
    # If new image to upload delete the old one first
    if request.files["picture"]:
        the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        oldimg = str(the_recipe['imgfullname'])
        path = os.getcwd()
        oldimgpath = path + "/static/images/" + oldimg
        os.remove(oldimgpath)

        # save the new image in the image dir
        image = request.files["picture"]
        ext = image.filename.rsplit(".", 1)[1]
        image_dir = path + "/static/images/" + str(ObjectId(recipe_id)) + "." + ext
        image.save(image_dir)
        
        # update the image name since it might have different extention
        newpicture = str(recipe_id) + "." + ext
        
        recipes.update_one({'_id': ObjectId(recipe_id)}, {"$set":
        {
            "imgfullname": newpicture
        }})

    return redirect(url_for('recipe', recipe_id = recipe_id))


# DELETE
@app.route('/delete_task/<recipe_id>')
def delete_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    
    # delete the image first
    oldimg = str(the_recipe['imgfullname'])
    path = os.getcwd()
    oldimgpath = path + "/static/images/" + oldimg
    os.remove(oldimgpath)

    # then we can delete the recipe in MongoDB
    mongo.db.recipes.delete_one({'_id': ObjectId(recipe_id)})
    return redirect(url_for('index'))




# OTHER TASKS

# SEARCH BAR
@app.route('/search', methods=["POST"])
def search():
    if request.method == "POST":
        data = request.form.to_dict()
        keyword = str(data['mysearch'])
        query={"ingredients": { "$regex": keyword, "$options": "i" }}
    return render_template("search.html", recipes=mongo.db.recipes.find(query))


# CONFIRMATION EMAIL SENT
@app.route('/sent')
def sent():
    return render_template("sent.html", recipes=mongo.db.recipes.find())




if __name__ =="__main__":
    app.run(host=os.getenv("IP"),
       port=int(os.getenv("PORT")),
       debug=True)



