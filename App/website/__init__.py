from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

#database object and name
db = SQLAlchemy()
DB_NAME = "database.db"

#create a flask application, initialize secret key and return it.
def create_app():
    app = Flask(__name__)
    #encrypt/secure the cookies and session data
    app.config['SECRET_KEY'] = 'lpfmdkmm doksmii'
    #sqlalchemy is stored/located at sqlite:///database.db
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    #register blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    #defines the user and notes class
    from .models import User, Settings

    create_database(app)

    login_manager = LoginManager()
    #redirect to auth.login is user is not logged in
    login_manager.login_view = 'auth.users'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
#checks if database exists and if it doesn't exist, creates one
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')