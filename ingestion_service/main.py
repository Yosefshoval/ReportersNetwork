from fastapi import FastAPI
import logging
from orchestrator import main_config, orchestrator
from os import getenv

images_folder = getenv('IMAGES_FOLDER_PATH', '../images/tweet_images')

logger = logging.getLogger('Ingestion service')
logging.basicConfig(level=logging.INFO)

app = FastAPI()


@app.get('/')
def home():
    logger.info('Home route clicked. service healthy.')
    return {
        'message' : 'server is running'
    }


@app.get('/images_loader')
def load_images():
    result = orchestrator.load_images_main_loop()
    return result