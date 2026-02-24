from http.client import responses
from config import IngestionConfig
import requests
from os import getenv

class MongoLoaderClient:
    """
    Client for communicate with MongoDB service.
    There should be saved binary images with image_id field.
    """

    def __init__(self):
        self.url = getenv('GRIDFS_URL')

    def save_binary_image(self, content: str | bytes, image_id):
        request_json = {'content' : content, 'image_id' : image_id}

        response = requests.post(
            url=self.url,
            json=request_json
        )
        return response.json()

client = MongoLoaderClient()