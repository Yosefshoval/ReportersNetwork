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

    def save_binary_image(self, file: bytes, image_id: str, image_name: str):
        files = {'file' : (image_name, file, 'image/png')}
        payload = {'image_id': image_id}

        response = requests.post(
            url=self.url,
            files=files,
            data=payload
        )
        IngestionConfig.logger.info(f'image with id {image_id} sent to mongodb server')
        IngestionConfig.logger.info(f'response: {response}')
        return response

client = MongoLoaderClient()