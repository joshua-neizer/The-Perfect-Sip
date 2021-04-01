#stores the standard routes for the website that the user can navigate to 

from flask import Flask, Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Settings, User
from . import db
import json
import requests
from flask_cors import CORS



#setup blueprint
views = Blueprint('views',__name__)
cors = CORS()
cors.init_app(views, resources={r"/*": {"origins": "*", "supports_credentials": True}})


@views.route('/', methods=['GET', 'POST'])

#cannot access home page unless user is logged in
@views.before_request
@login_required
#this function will run when user directs to /
def home():
     
    temperature = request.form.get('select-temperature')
    perfect = request.form.get('P_RGB')
    cold = request.form.get('C_RGB')
    hot = request.form.get('H_RGB')
    currTemp = request.form.get('temp')
    tempRange = request.form.get('select-range')
    userList = User.query.all()
    #print(perfect)
    if(request.method == 'POST'):
        temperature = int(temperature)
        #pcolor = tuple(int(perfect[i:i+2], 16) for i in (0, 2, 4))
        print(tempRange)
        print(perfect)
        if int(temperature) > 80:
            flash('Temperature too high!', category='error')
        if int(temperature) < 60:
            flash('Temperature too low!', category='error')
        else:
            r = requests.post('http://184.148.145.47:5000/users', params={'user': current_user.first_name, 'des_temp': temperature, 'P_RGB' : perfect, 'C_RGB': cold, 'H_RGB': hot, 'range': tempRange, 'temp': currTemp})
            new_setting = Settings(temperature=temperature,perfect=perfect,user_id=current_user.id, cold=cold, hot=hot)
            db.session.add(new_setting)
            db.session.commit()
            flash('Setting added!', category='success')
            return render_template("home.html", user=current_user, temperature=temperature, perfect = perfect, cold = cold, hot = hot, currTemp = currTemp)

    if (request.method == 'GET'):
        r = requests.get('http://184.148.145.47:5000/users/' + current_user.first_name)
        data = r.json()
        #print(data)
        current_temp = data['data']['temperature']
        current_vol = data['data']['volume']
        #current_amount = r.json.user


        return render_template("home.html", user=current_user, currTemp=current_temp, currVolume=current_vol)

        
    #, user=current_user, curTemp = temperature)
'''
    if(request.method == 'GET'):

        r = requests.get('http://184.148.145.47:5000/users/' + current_user.first_name)
        #current_temp = r.json.des_temp
        #current_amount = r.json.user
    
    #references current user and checks if it is authenticated
    return render_template("home.html", user=current_user, curTemp = current_temp)
'''





'''
async def asynchronous():
        async with aiohttp.ClientSession() as session:

        api_url = 'http://184.148.145.47:5000/users' + current_user.first_name
        async with session.get(api_url) as resp:
            settings = await resp.json()
            username = settings['user']
            temperature = settings['temperature']
'''



