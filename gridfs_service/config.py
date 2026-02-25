import os

class Config:
    server_port = os.getenv('GRIDFS_PORT')
    mongo_url = os.getenv('MONGO_URI')
    mongo_db = os.getenv('MONGODB_DATABASE')
    mongo_coll = os.getenv('MONGODB_COLLECTION')

