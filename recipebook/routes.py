from flask import render_template, request, redirect, url_for
from recipebook import app, db
from recipebook.models import Category, Recipe

@app.route("/")
def home():
    recipies = list(Recipe.query.order_by(Recipe.id).all())
    return render_template("recipies.html", recipies=recipies)


@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))



@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        recipe = Recipe(
            recipe_name=request.form.get("recipe_name"),
            recipe_description=request.form.get("recipe_description"),
            recipe_method=request.form.get("recipe_method"),
            recipe_time=request.form.get("recipe_time"),
            category_id=request.form.get("category_id")
        )
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_recipe.html", categories=categories)


@app.route("/edit_recipe/<int:recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        recipe.recipe_name = request.form.get("recipe_name")
        recipe.recipe_description = request.form.get("recipe_description")
        recipe.recipe_method = request.form.get("recipe_method")
        recipe.recipe_time = request.form.get("recipe_time")
        recipe.category_id = request.form.get("category_id")
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit_recipe.html", recipe=recipe, categories=categories)



@app.route("/delete_recipe/<int:recipe_id>")
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for("home"))



'''
@app.route("/register", methods=["GET", "POST"])
def register():
    
'''