#stores the standard routes for the website that the user can navigate to 

from flask import Flask, Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Settings, User
from . import db
import json
import requests

#setup blueprint
views = Blueprint('views',__name__)
current_temperature = 0
coffee_amount = 0

@views.route('/', methods=['GET', 'POST'])
#cannot access home page unless user is logged in
@login_required
#this function will run when user directs to /
def home():
    if(request.method == 'POST'):
        temperature = int(request.form.get('select-temperature'))
        ledcolor = request.form.get('led-color')
        lcolor = tuple(int(ledcolor[i:i+2], 16) for i in (0, 2, 4))

        if int(temperature) > 80:
            flash('Temperature too high!', category='error')
        if int(temperature) < 60:
            flash('Temperature too low!', category='error')
        else:
            r = requests.post('http://184.148.145.47:5000/users', params={'user': current_user.first_name, 'des_temp': temperature, 'P_RGB' : lcolor})
            flash('Setting added!', category='success')
            '''
            new_setting = Settings(temperature=temperature,ledcolor=ledcolor,user_id=current_user.id)
            db.session.add(new_setting)
            db.session.commit()
            flash('Setting added!', category='success')
            '''
    if(request.method == 'GET'):

        r = requests.get('http://184.148.145.47:5000/users/' + current_user.first_name)
        current_temp = r.json.temperature
        current_amount = r.json.user
    
    #references current user and checks if it is authenticated
    return render_template("home.html", user=current_user, curTemp = current_temp)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
'''
async def asynchronous():
        async with aiohttp.ClientSession() as session:

        api_url = 'http://184.148.145.47:5000/users' + current_user.first_name
        async with session.get(api_url) as resp:
            settings = await resp.json()
            username = settings['user']
            temperature = settings['temperature']
'''



