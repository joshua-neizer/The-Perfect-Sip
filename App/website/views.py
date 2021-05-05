# Stores the standard routes for the website that the user can navigate to 

from flask import Flask, Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Settings, User
from . import db
import json
import requests
from flask_cors import CORS

# Setup blueprint
views = Blueprint('views',__name__)
cors = CORS()
cors.init_app(views, resources={r"/*": {"origins": "*", "supports_credentials": True}})

@views.route('/', methods=['GET', 'POST'])

#cannot access home page unless user is logged in
@views.before_request
@login_required

# This function will run when user directs to /
def home():
    # Gets the information from the forms
    temperature = request.form.get('select-temperature')
    perfect = request.form.get('P_RGB')
    cold = request.form.get('C_RGB')
    hot = request.form.get('H_RGB')
    currTemp = request.form.get('temp')
    tempRange = request.form.get('select-range')

    # POST Request Definition
    if(request.method == 'POST'):
        temperature = int(temperature)
        if int(temperature) > 80:
            flash('Temperature too high!', category='error')
        if int(temperature) < 60:
            flash('Temperature too low!', category='error')
        else:
            r = requests.post('http://192.168.2.100:5000/users', params={'user': current_user.first_name, 'des_temp': temperature, 'P_RGB' : perfect, 'C_RGB': cold, 'H_RGB': hot, 'range': tempRange, 'temp': currTemp})
            new_setting = Settings(temperature=temperature,perfect=perfect,user_id=current_user.id, cold=cold, hot=hot)
            db.session.add(new_setting)
            db.session.commit()
            flash('Setting added!', category='success')
            return render_template("home.html", user=current_user, temperature=temperature, tempRange = tempRange, perfect = perfect, cold = cold, hot = hot, currTemp = currTemp)

    # GET Request Definition
    if (request.method == 'GET'):
        r = requests.get('http://192.168.2.100:5000/users/' + current_user.first_name)
        data = r.json()
        current_temp = data['data']['temperature']
        current_vol = data['data']['volume']

        return render_template("home.html", user=current_user, currTemp=current_temp, currVolume=current_vol)

    return render_template("home.html", user=current_user, temperature=temperature,  tempRange = tempRange, perfect = perfect, cold = cold, hot = hot, currTemp = currTemp)

@views.route('/delete-user', methods=['DELETE'])
def delete_user():
    note = json.loads(request.data)
    userId = note['userId']
    user = User.query.get(userId)
    if user:
        db.session.delete(user)
        db.session.commit()
        
    return jsonify({})