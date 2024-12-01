from flask import Flask
from flask_restx import Api
from order_service.app.routes import api as order_api
from pymongo import MongoClient

def create_app():
    app = Flask(__name__)
    app.config.from_object('order_service.app.config.Config')
    api = Api(app)
    api.add_namespace(order_api, path='/orders')
    
    # Initialize MongoDB client
    mongo_client = MongoClient(app.config['MONGO_URI'])
    app.mongo_client = mongo_client
    app.db = mongo_client[app.config['DATABASE_NAME']]
    app.orders_collection = app.db['orders']
    
    return app