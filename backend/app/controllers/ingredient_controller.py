from flask import Blueprint, jsonify, request

from .. import db
from ..models.Ingredient import Ingredient

ingredient_blueprint = Blueprint("ingredient", __name__)


@ingredient_blueprint.route("/ingredient", methods=["POST"])
def create_ingredient():
    try:
        data = request.get_json()
    except:
        return jsonify({"message": "Invalid data"}), 400

    try:
        new_ingredient = Ingredient(data["name"], data["isHarmful"], data["harmfulSkin"])
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


@ingredient_blueprint.route("/ingredient", methods=["DELETE"])
def delete_ingredient():
    try:
        data = request.get_json()
    except:
        return jsonify({"message": "Invalid data"}), 400

    try:
        ingredient = Ingredient.query.filter_by(id=data["id"]).first()
        db.session.delete(ingredient)
        db.session.commit()
        return jsonify({"message": "Ingredient deleted"}), 200
    except:
        return jsonify({"message": "An error occurred deleting the ingredient"}), 500


@ingredient_blueprint.route("/ingredient/compare", methods=["POST"])
def compare_ingredients():
    """
    Input:
        skinType: string
        ingredients: list of strings (comma separated)
    Output:
        list of ingredients that are harmful to the skinType
    """
    skin_types = ["yağlı cilt", "kuru cilt", "karma cilt"]

    all_ingredients_in_db = Ingredient.query.all()
    harmful_ingredients = [] # list of harmful ingredients for the skin type
    gozenek_tikayici_ingredients = [] # list of pore clogging ingredients for the skin type
    try:
        data = request.get_json()
        skin_type = data["skinType"]
        ingredients = data["ingredients"]
        ingredients = [ingredient.strip() for ingredient in ingredients.split(",")]
        if skin_type.lower() not in skin_types:
            return jsonify({"message": "Invalid skin type"}), 400
        for ingredient in ingredients:
            for db_ingredient in all_ingredients_in_db:
                if db_ingredient.name.lower() == ingredient.lower():
                    if db_ingredient.isHarmful and skin_type.lower() in db_ingredient.harmfulSkin.lower():
                        harmful_ingredients.append(db_ingredient.name)
                    elif db_ingredient.isHarmful and "gözenek tıkayıcı" in db_ingredient.harmfulSkin.lower():
                        gozenek_tikayici_ingredients.append(db_ingredient.name)

        harmful_ingredients_message = f"Seçtiğiniz cilt tipi '{skin_type}' için zararlı olan içerikler: "
        for ingredient in harmful_ingredients:
            harmful_ingredients_message += ingredient + ", "
        if len(harmful_ingredients) == 0:
            harmful_ingredients_message += "Bulunmamaktadır."
        gozenek_tikayici_ingredients_message = f"Seçtiğiniz cilt tipi '{skin_type}' için gözenek tıkayıcı olan içerikler: "
        for ingredient in gozenek_tikayici_ingredients:
            gozenek_tikayici_ingredients_message += ingredient + ", "
        if len(gozenek_tikayici_ingredients) == 0:
            gozenek_tikayici_ingredients_message += "Bulunmamaktadır."
        return jsonify({"harmfulIngredients": harmful_ingredients_message, "gozenekTikayiciIngredients": gozenek_tikayici_ingredients_message}), 200
    except:
        return jsonify({"message": "Invalid data"}), 400
