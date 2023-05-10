from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os


def get_mongo_db_connection():
    mongo_pass = os.getenv('MONGO_PASS')
    uri = f'mongodb+srv://track-trace-integration-user:{mongo_pass}@cluster0.ait8u8g.mongodb.net/?retryWrites=true&w=majority'

    client = MongoClient(uri, server_api=ServerApi('1'))

    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except Exception as e:
        print(e)
