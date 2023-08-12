from flask import render_template
from recipebook import app, db
from recipebook.models import Category, Recipe

@app.route("/")
def home():
    return render_template("recipies.html")


