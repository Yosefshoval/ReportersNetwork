from pymongo import MongoClient
from config import Config
from gridfs import GridFS
from logging import Logger
import io

class MongoOperations:
    def __init__(self, logger: Logger):
        self.logger = logger
        self.client = MongoClient(Config.mongo_url)


    def get_gridfs_collection(self):
        db = self.client[Config.mongo_db]
        fs_coll = GridFS(db)
        return fs_coll


    def insert_bin_image(self, binary_image: io.BytesIO, image_id: str, image_name: str):
        fs = self.get_gridfs_collection()
        self.logger.info('get_gridfs_collection')
        try:
            file_id = fs.put(binary_image,
                             filename=image_name,
                             metadata={'image_id' : image_id}
                             )
        except Exception as e:
            self.logger.error(e)
            raise e

        self.logger.info(f'image {image_name} inserted successfully into the gridfs. new id: {file_id}')
        return True


    def find_image(self, image_id: str):
        fs = self.get_gridfs_collection()
        binary_image = fs.find_one({'description': image_id})
        return binary_image