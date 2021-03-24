# Acts as the REST API back-end to accept GET, POST, and DELETE requests

import markdown
import os
import shelve
import pickle
from Hash import Hash

# Import the framework
from flask import Flask, g
from flask_restful import Resource, Api, reqparse

# Create an instance of Flask
app = Flask(__name__)

#Creat the API
api = Api(app)

# Loads the saved hashmap to continue where the API left off
hashUser = pickle.load( open( "data/hash_map.p", "rb" ) )

settings = ['temperature', 'LED']

# function freezes and saves the hashmap object to a pickle file
def saveData():
    pickle.dump(hashID, open("data/hash_map.p", "wb") )

# function opens the photos database file to be interacted with
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("user_data.db")
    return db 

def update_state(data):
    pass

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    '''Present some documentation'''

    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        # Read the conetnet of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)

# Object allows GET and POST requests for the entire database
class UserData(Resource):

    # GET request to photos returns the JSON for all of the photos in the database
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())
        
        users = []

        for key in keys:
            users.append(shelf[key])
        
        # On success, returns a 200 status
        return {'message': 'Success', 'data' : users}, 200
    

    # POST request to photos appends new photo to the database
    def post(self):
        parser = reqparse.RequestParser()
        shelf = get_db()

        # Parses the request for given arguments
        parser.add_argument('user', required=True)

        #Parse the arguments into an object
        args = parser.parse_args()

        user = args ['user']

        if hasUser.search(user) == -1:
            hashUser.generate(user)
            
            data = {}

            for key in settings:
                data [key] = None

            shelf[user] = data
        
        else:
            userData = shelf[hashUser.search(user)]

            keys = list(args.keys()).remove('user')

            for key in keys:
                try: 
                    shelf [user] [key] == arg [key]
                except:
                    pass
        
        # Freezes and saves the hashmap object to the pickle file
        saveData()
        
        # On success, returns a 201 status
        return {'message' : 'User data updated', 'data' : args}, 201


# Object allows GET and DELETE requests for specific photos
class User(Resource):
    # GET request to photos returns the JSON for all of the photos in the database
    def get(self, user):
        shelf = get_db()
        
        if hasUser.search(user) == -1:
            return {'message': 'User Not Found', 'data' : {}}, 200
        
        
        # On success, returns a 200 status
        return {'message': 'User Found', 'data' : shelf[hashUser.search(user)]}, 200


    # DELETE request deleetes photo from the database based on identifier
    def delete(self, user):
        # Deletes identfier from hashmap and saves the object
        if hasUser.search(user) == -1:
             return {'message':'User not found', 'data':{}}, 404

        userID = hasUser.search(user)

        hashID.array [userID] = -1
        saveData()

        shelf = get_db()
           

        del shelf[userID]
        
        # On success, returns 204 status
        return '', 204

api.add_resource(PhotoList, '/photos')
api.add_resource(Photo, '/photos/<string:identifier>')
