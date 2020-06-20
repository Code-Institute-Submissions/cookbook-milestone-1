import os
from flask import Flask, render_template

app = Flask(__name__)


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

@app.route('/profile')
def profile():
    return render_template("profile.html")









if __name__ =="__main__":
    app.run(host=os.getenv("IP"),
       port=int(os.getenv("PORT")),
       debug=True)



"""
if __name__ == "__main__":
  app.run(debug=True)
"""