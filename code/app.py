from datetime import timedelta

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user_register import UserRegister
from item import Item, ItemList

app = Flask(__name__)
app.secret_key = 'pyziko'
api = Api(app)

# todo INFO: check bookmark :PYTHON/FLASK/Flask-JWT CONFIGURATION
# app.config['JWT_EXPIRATION_DELTA'] = timedelta(weeks=1)
jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)  # debug+True helps to debug
