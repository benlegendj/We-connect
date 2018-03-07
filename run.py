from models import User
from models import Business
import json
from flask import Flask , request
from flask_restplus import Resource, Api, fields

app = Flask(__name__)

authorizations={
    'apikey':'apikey',
    'in':'header',
    'name': 'X-API-KEY'

}




api = Api(app, version='1.0', title='Weconnect API',
          description='A simple Weconnect API endpoints',authorizations=authorizations)

ns = api.namespace('todos', description='TODO operations')

#new user registration
new_user = api.model('New User', {
    'id': fields.Integer(unique=True, description='This is the unique user id'),
    'name': fields.String(required=True, description='Enter your username'),
    'password': fields.String(required=True,
                              description='this is the password that will be used to enable the user to Log in')
})
#user login 
user_login = api.model('User Login', {
    'username': fields.String(required=True, description='Enter your username'),
    'password': fields.String(required=True, description='Enter your password')
})

#new business registration
new_business = api.model('New User', {
    'business_id': fields.Integer(unique=True, description='This is the unique user id'),
    'business_name': fields.String(required=True, description='Enter your username'),
    'business_location': fields.String(required=True,
                              description='this is the password that will be used to enable the user to Log in'),
    'business_description': fields.String(required=True, description='the business description here')                       
})
#creating new users
ben = User()
ben1 = User()
ben.create({"name": "bene", "password": "rest1"})
ben1.create({"name": "andela", "password": "rest1"})

#user registration route
@api.route('/auth/register')
@api.expect(new_user)
class CreateUser(Resource):
    def post(self):
        User.all_users.append(api.payload)
        return {"message": "user registered succesfully"}, 201

    def get(self):
        return User.all_users


@api.route('/auth/login')
@api.expect(user_login)
class LoginUser(Resource):
    def post(self):
        return {}


@api.route('/auth/logout')
class Logout(Resource):
    def post(self):
        return {"message": "logout successful"}


@api.route('/auth/reset-password')
class ResetPassword(Resource):
    def post(self):
        return {"message": "password reset done successfully"}



@api.route('/auth/business')
@api.expect(new_business)
class CreateUser(Resource):
    def post(self):   
        return {"message": "business created succesfully"},201  


if __name__ == '__main__':
    app.run(debug=True)
