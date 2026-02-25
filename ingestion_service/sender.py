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

    def save_binary_image(self, content: bytes, image_id, image_name: str):
        request_json = {'content' : content.decode('utf-8', errors='replace'), 'image_id' : image_id, 'image_name' : image_name}

        response = requests.post(
            url=self.url,
            json=request_json
        )
        return response.json()

client = MongoLoaderClient()