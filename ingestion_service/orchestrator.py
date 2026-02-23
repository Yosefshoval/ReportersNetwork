from ocr import OCREngine, MetadataExtractor
from producer import producer
from sender import client
import os
from pathlib import Path
import logging
import uuid


logger = logging.getLogger('Ingestion service')
logging.basicConfig(level=logging.INFO)


class IngestionConfig:
    images_folder_path = Path(os.getenv('IMAGES_FOLDER_PATH'))
    kafka_url = os.getenv('KAFKA_URL')
    kafka_topic = os.getenv('KAFKA_TOPIC')
    server_port = os.getenv('SERVER_PORT')


def throw_exceptions(name, operation):
    if not operation:
        raise Exception(f'Error when trying do {name} operation.')



class IngestionOrchestrator:
    """
    manger the service:
    GET request is a trigger, images folder load into the system,
    for each image: metadata and text extracted from the image.
    send each one to Kafka via producer, and save binary image in MongoDB.
    """


    @staticmethod
    def load_images_main_loop():
        metadata_extractor = MetadataExtractor()
        ocr_engine = OCREngine()

        images_directory = IngestionConfig.images_folder_path
        images_handled_successfully = 0

        for image in images_directory.rglob("*"):
            if not image.is_file():  # Check if it is a file
                logger.error(f'{file_path} is not a file')
                continue
            try:
                image_id = uuid.uuid4()
                image_path = str(image)

                # 1: extract metadata
                ocr_engine.extract_text(image_path=image_path)

                # 2: extract text
                metadata = metadata_extractor.extract_metadata(image_path=image_path)

                # 3: send to mongodb
                # binary_image = metadata_extractor.get_binary_content(image_path)
                # sent = client.save_binary_image(binary_image, image_id)
                # throw_exceptions('send content to mongodb service', sent)

                # 4: send to kafka
                metadata['image_id'] = image_id
                published = producer.publish(metadata)
                throw_exceptions('publish message', published)

                images_handled_successfully += 1
            except Exception as e:
                logger.error(e)

        return {
            'images handled successfully': images_handled_successfully
        }

main_config = IngestionConfig() #TODO: fill this up

orchestrator = IngestionOrchestrator() #TODO: fill this up