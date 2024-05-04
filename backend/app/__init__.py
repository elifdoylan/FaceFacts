import os
from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS

from .database import db
# from .controllers.blog_controller import blog_blueprint
# from .controllers.ingredient_controller import ingredient_blueprint

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///default.db"

    # .env dosyasını yükle
    load_dotenv()

    # .env dosyasından yapılandırma ayarlarını al
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")

    # Veritabanı bağlantısını başlat
    db.init_app(app)


    # CORS desteğini etkinleştir
    # CORS(app, supports_credentials=True)


    from .controllers.blog_controller import blog_blueprint
    from .controllers.ingredient_controller import ingredient_blueprint
    


    # Blueprintleri kaydet
    app.register_blueprint(blog_blueprint, url_prefix='/')
    app.register_blueprint(ingredient_blueprint)
    # app.register_blueprint(views, url_prefix='/')
    # return app
    
    with app.app_context():
        
        # from .models import Blog, Ingredient
        from .models import Blog
        
        db.create_all()
        
    return app


    CORS(app, supports_credentials=True)

    from .routes import init_app
    init_app(app)
    


    app.register_blueprint(blog_blueprint)
    app.register_blueprint(ingredient_blueprint)

    return app




