from flask import render_template, request, redirect, url_for, session, flash
from recipebook import app, db
from recipebook.models import Category, Recipe, Users
from werkzeug.security import generate_password_hash, check_password_hash

@app.route("/")
def home():
    recipies = list(Recipe.query.order_by(Recipe.id).all())
    return render_template("recipies.html", recipies=recipies)


@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)

# allows user to add category
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        # checks if category name already exists
        exists = list(Category.query.filter_by(category_name=request.form.get("category_name", '')))
        if len(exists) > 0:
            # flash message if category name already exists - page will reload
            flash("This Categeory name already exists")
        else:
            category = Category(category_name=request.form.get("category_name"))
            db.session.add(category)
            db.session.commit()
            return redirect(url_for("categories"))
    return render_template("add_category.html")

# allows user to edit category name
@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        exists = list(Category.query.filter_by(category_name=request.form.get("category_name", '')))
        if len(exists) > 0:
            # message flash if category name alredy exists
            flash("This Categeory name already exists")
        else:
            category.category_name = request.form.get("category_name")
            db.session.commit()
            return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)

# allows user to delete a category
@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))


# allows user to add recipe also checks if recipe name already used
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        recipe = Recipe(
            recipe_name=request.form.get("recipe_name"),
            recipe_description=request.form.get("recipe_description"),
            recipe_ingredients=request.form.get("recipe_ingredients"),
            recipe_method=request.form.get("recipe_method"),
            recipe_time=request.form.get("recipe_time"),
            recipe_image=request.form.get("recipe_image"),
            category_id=request.form.get("category_id")
        )
        # user informed if recipe name already in use 
        exists = list(Recipe.query.filter_by(recipe_name=request.form.get("recipe_name", '')))
        if len(exists) > 0:
            #message flashed and page reloaded if name already exists
            flash("This Recipe name already exists")
        else:
            db.session.add(recipe)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("add_recipe.html", categories=categories)

# allows user to edit recipes
@app.route("/edit_recipe/<int:recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        recipe.recipe_description = request.form.get("recipe_description")
        recipe.recipe_ingredients = request.form.get("recipe_ingredients")
        recipe.recipe_method = request.form.get("recipe_method")
        recipe.recipe_time = request.form.get("recipe_time")
        recipe.recipe_image = request.form.get("recipe_image")
        recipe.category_id = request.form.get("category_id")
        exists = list(Recipe.query.filter_by(recipe_name=request.form.get("recipe_name", '')))
        if len(exists) > 0:
            flash("This Recipe name already exists")
        else:
            recipe.recipe_name = request.form.get("recipe_name")
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("edit_recipe.html", recipe=recipe, categories=categories)


# allows the user to delete recipe
@app.route("/delete_recipe/<int:recipe_id>")
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for("home"))

# sign in/ sign up and sign out code was adapted from code challanges from this course and stackoverflow
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = Users.query.filter(Users.user_name == \
                                           request.form.get("username").lower()).all()
        
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("signup"))
        
        user = Users(
            user_name=request.form.get("username").lower(),
            password=generate_password_hash(request.form.get("password"))
        )
        
        db.session.add(user)
        db.session.commit()

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("signup.html")


@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        # check if username exists in db
        existing_user = Users.query.filter(Users.user_name == \
                                           request.form.get("username").lower()).all()

        if existing_user:
            print(request.form.get("username"))
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user[0].password, request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("signin"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("signin"))

    return render_template("signin.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
        
    if "user" in session:
        return render_template("profile.html", username=session["user"])

    return redirect(url_for("signin"))


@app.route("/signout")
def signout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("signin"))

# allows users to view recipes 
@app.route("/view_recipe/<int:recipe_id>", methods=["GET"])
def view_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return render_template("view_recipe.html", recipe=recipe)

