import os

from dotenv import load_dotenv, find_dotenv
from flask import Flask
from flask_cors import CORS

from .database import db
from .controllers.blog_controller import blog_blueprint
from .controllers.ingredient_controller import ingredient_blueprint


load_dotenv(find_dotenv())


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///default.db"
    app.config["SQLALCHEMY_BINDS"] = {
        "blogs": os.getenv("SQLALCHEMY_DATABASE_URI_BLOGS"),
        "ingredients": os.getenv("SQLALCHEMY_DATABASE_URI_INGREDIENTS"),
    }
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv(
        "SQLALCHEMY_TRACK_MODIFICATIONS"
    )

    db.init_app(app)

    with app.app_context():
        
        from .models import Blog, Ingredient
        db.create_all()


    CORS(app, supports_credentials=True)

    from .routes import init_app
    init_app(app)

    app.register_blueprint(blog_blueprint)
    app.register_blueprint(ingredient_blueprint)

    return app