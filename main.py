from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class DB_LOGIN(Resource):
    def get(self):
        return {'':''}

class BA_RFO(DB_LOGIN):
    def get(self):
        return {'password': 'rfo heslo'}     
    
class BA_ISKN(DB_LOGIN):
    def get(self):
        return {'password': 'heslo'}
    
class BA_NEV(DB_LOGIN):
    def get(self):
        return {'password': 'heslo'}
    
class BA_RA(DB_LOGIN):
    def get(self):
        return {'password': 'ra heslo'}

class BA_SODB(DB_LOGIN):
    def get(self):
        return {'password': 'heslo'}
    

api.add_resource(BA_RFO, '/rfo')
api.add_resource(BA_RA, '/ra')

if __name__ == '__main__':
     app.run(port='5002')