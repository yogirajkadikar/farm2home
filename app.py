from flask import Flask,request #Capital Flask is a class in python package flask
from flask_restful import Resource, Api
from flask_jwt import JWT , jwt_required

from security import authenticate, identity

app = Flask(__name__) #Class is initialised in variable called app, dunder name is used to notify class Flask where it will run
app.secret_key = 'yogi'
api = Api(app)
# @app.route('/') #decorator
# def home():   #method assissgnment
#     return "Hello, World!"

jwt = JWT(app, authenticate, identity)

items = []
class Item(Resource):
    @jwt_required()
    def get(self,name):
        item = next(filter(lambda x: x['name']== name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self,name):
        if next(filter(lambda x: x['name']== name, items), None):
            return {'message': "An item with {} name already exists".format(name)}, 400

        data = request.get_json()
        item = { 'name': name, 'price' : data['price']}
        items.append(item)
        return item, 201

    def delete(self,name):
        global items
        items = list(filter(lambda x:x['name'] != name,items))
        return {'message': 'Item deleted'}

class Items_List(Resource):
    def get(self):
        return {'items': items}
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items_List, '/items/')
app.run(port=5000, debug=True)
