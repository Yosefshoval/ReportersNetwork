import logging
import os
from pathlib import Path


class IngestionConfig:
    images_folder_path = Path(os.getenv('IMAGES_FOLDER_PATH'))

    kafka_url = os.getenv('KAFKA_URL')
    kafka_topic = os.getenv('KAFKA_TOPIC')
    server_port = os.getenv('SERVER_PORT')

    logger = logging.getLogger('Ingestion service')
    logging.basicConfig(level=logging.INFO)
