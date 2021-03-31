from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
#allows to hash password so it is not stored in plain text
#a hashing function is a one way function
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
#flask log in module
from flask_login import login_user, login_required, logout_user, current_user
import requests
#setup blueprint
auth = Blueprint('auth',__name__)

#methods lists the type of requests this route can accept
#when submit button is clicked, that is a post request that sends information to the server 
@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        #check if user is valid - querying the database's email field
        user = User.query.filter_by(email=email).first()

        #if user is found, check if password is equal to hash stored on server

        if user:
            #if hashes are the same
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                #remember = True, stored in flask session so user doesn't have to constantly keep logging on
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('Email does not exist', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required #decorator that make sure user cannot access this page unless they are logged in
def logout():
    logout_user()
    #signs out user and returns them to login page
    return redirect(url_for('auth.login'))


@auth.route('/switch')
def users():
    userList = User.query.all()
    users = []
    emails = []
    for x in userList:
        print(x.first_name)
        users.append(str(x.first_name))
    for x in userList:
       
        emails.append(str(x.email))

    length = len(userList)
    db.session.commit()
    #print(userList)
    if request.method == 'GET':
        
        return render_template("users.html", user=current_user.first_name,users = users,length = length, emails = emails)#, users=current_user)


@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method =='POST':
        email = request.form.get('email')
        firstName =request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #query database to check if email already exists
        user = User.query.filter_by(email=email).first()
        if user: 
            flash('Email already exists, use another one', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 character', category='error')
        elif (password1!=password2):
            flash('Passwords do not match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least seven characters', category='error')
        else: 
            #create new user
            new_user = User(email=email,first_name=firstName, password = generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            #login_user(user, remember=True)
            flash('Account created!', category='success')
            # views is the blueprint name and home is the function name that redirects to home page
            return redirect('/login')#url_for('views.home'))

    return render_template("sign-up.html", user=current_user)