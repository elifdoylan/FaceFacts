from flask import Blueprint, jsonify, request

from .. import db
from ..models.Blog import Blog

blog_blueprint = Blueprint("blog", __name__)

@blog_blueprint.route("/blogs", methods=["POST"])
def create_blog():
    try:
        data = request.get_json()
    except:
        return jsonify({"message": "Invalid data"}), 400

    try:
        new_blog = Blog(title=data["title"], content=data["content"], author=data["author"])
        db.session.add(new_blog)
        db.session.commit()
        return jsonify(new_blog.json()), 201
    except:
        return jsonify({"message": "An error occurred creating the blog"}), 500

@blog_blueprint.route("/blogs", methods=["GET"])
def get_blogs():
    try:
        blogs = Blog.query.all()
        return jsonify([blog.json() for blog in blogs]), 200
    except:
        return jsonify({"message": "An error occurred retrieving the blogs"}), 500


@blog_blueprint.route("/blogs", methods=["DELETE"])
def delete_blog():
    try:
        data = request.get_json()
    except:
        return jsonify({"message": "Invalid data"}), 400

    try:
        blog = Blog.query.filter_by(id=data["id"]).first()
        db.session.delete(blog)
        db.session.commit()
        return jsonify({"message": "Blog deleted"}), 200
    except:
        return jsonify({"message": "An error occurred deleting the blog"}), 500
