import requests
from os import getenv

class MongoLoaderClient:
    """
    Client for communicate with MongoDB service.
    There should be saved binary images with image_id field.
    """

    def __init__(self):
        self.url = getenv('GRIDFS_URL')

    def save_binary_image(self, content: str | bytes):
        pass

client = MongoLoaderClient()