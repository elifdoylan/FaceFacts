from flask import Blueprint, jsonify, request, render_template
from .. import db  
from ..models import Blog



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

@blog_blueprint.route("/anasayfa", methods=["GET"])
def get_blogs():
    
    return render_template("index.html")
    # try:
    #     blogs = Blog.query.all()
    #     return jsonify([blog.json() for blog in blogs]), 200
    # except:
    #     return jsonify({"message": "An error occurred retrieving the blogs"}), 500


@blog_blueprint.route("/blog", methods=["GET"])
def get_ingredients():
    try:
        Blogs = Blog.query.all()  # Tüm Not nesnelerini alın
        Blog_data = [Blog.data for Blog in Blogs]  # Her bir Not nesnesinin `data` özelliğini alın
        return render_template("icerik.html", Blogs=Blog_data)  # `Blog_data` listesini render_template'e geçirin
    except Exception as e:
        return f"An error occurred: {str(e)}"
