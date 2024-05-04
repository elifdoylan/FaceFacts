from flask import Blueprint, jsonify, request, render_template

from .. import db  
# from ..models import Ingredient
from ..models import Blog

ingredient_blueprint = Blueprint("ingredient_blueprint", __name__)




@ingredient_blueprint.route("/ingredient", methods=["GET"])
def create_ingredient():
    try:
        data = request.get_json()
    except:
        return jsonify({"message": "Invalid data"}), 400

    try:
        new_ingredient = Ingredient(data["name"], data["isHarmful"])
        db.session.add(new_ingredient)
        db.session.commit()
        return jsonify(new_ingredient.json()), 201
    except:
        return jsonify({"message": "An error occurred creating the ingredient"}), 500
            
