from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/breakfast')
def breakfast():
    return render_template("breakfast.html")


@app.route('/lunch')
def lunch():
    return render_template("lunch.html")


@app.route('/dinner')
def dinner():
    return render_template("dinner.html")


@app.route('/dessert')
def dessert():
    return render_template("dessert.html")


@app.route('/drinks')
def drinks():
    return render_template("drinks.html")


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