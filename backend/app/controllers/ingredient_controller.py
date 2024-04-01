from flask import Blueprint, jsonify, request

from .. import db  
from ..models import Ingredient

ingredient_blueprint = Blueprint("ingredient", __name__)


@ingredient_blueprint.route("/ingredient", methods=["POST"])
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
    


@ingredient_blueprint.route("/ingredient", methods=["GET"])
def get_ingredients():
    try:
        ingredients = Ingredient.query.all()
        return jsonify([ingredient.json() for ingredient in ingredients]), 200
    except:
        return jsonify({"message": "An error occurred retrieving the ingredients"}), 500
