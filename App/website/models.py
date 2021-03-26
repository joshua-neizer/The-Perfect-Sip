#creating the database models for users and notes
from . import db
#module helps to log users in and user objects needs to inherit from UserMixin
from flask_login import UserMixin
from sqlalchemy.sql import func

#foreign key is a column in a database that references a column in another database

class Settings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Integer)
    ledcolor = db.Column(db.String(1000))
    #stores current date and time of note with note object
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    #foreign key ensures a valid id of an existing user is passed to this field.
    #One (user) to many (settings) relationship. 
    #reference the primary key of the user object -> id  
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    #unique identifier
    id = db.Column(db.Integer, primary_key=True)
    #no two users can have the same email
    email = db.Column(db.String(150),unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    #stores all the notes that the user owns
    settings = db.relationship('Settings')
