from recipebook import db

class Category(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(30), unique=True, nullable=False)
    recipe = db.relationship("Recipe", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.category_name



class Recipe(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(60), unique=True, nullable=False)
    recipe_description = db.Column(db.Text, nullable=False)
    recipe_method = db.Column(db.Text, nullable=False)
    recipe_time = db.Column(db.Time, nullable=False)
    recipe_image = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)
    users_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)



    def __repr__(self):
        return f"#{self.id} - Recipe:{self.recipe_name} | Time: {self.recipe_time}"


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(260), nullable=False)
    recipe = db.relationship("Recipe", backref="users", cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.user_name