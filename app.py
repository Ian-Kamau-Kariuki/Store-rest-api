import os

from flask import Flask
from flask_restful import  Api
from flask_jwt_extended import JWTManager


from resources.user import UserRegister, User, UserList,UserLogin
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'ian'
api = Api(app)

jwt = JWTManager(app) 


api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserList, '/users')
api.add_resource(UserLogin, '/login')

if __name__ == '__main__': #prevents running of app from another file importing app.py
    from db import db  #preventsncircular imports
    db.init_app(app)
    app.run(debug=True)  # important to mention debug=True

    