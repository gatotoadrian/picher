import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from os import path
app = Flask(__name__)


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '0b6bd163c27f7d7512077a91'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://irhbzsslwwjlid:84700a835c2958615dfca352a0a330b8c168b3ddacec52bb78d5b4a5327d8bf2@ec2-54-158-247-210.compute-1.amazonaws.com:5432/da2e41gniio6s9'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///account.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'gatotoadrian@gmail.com'
    app.config['MAIL_PASSWORD'] = 'adrianeddie8113'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    
    db.init_app(app)

    from .views import views
    from .auth import auth
    

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")


    from .models import User, Post, Comment, Like

    create_database(app)
    

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists("app/" + "account.db"):
        db.create_all(app=app)
        print("Created database!")

        