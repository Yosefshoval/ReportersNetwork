from ocr import OCREngine, MetadataExtractor
from producer import producer
from sender import client
import os
from pathlib import Path
import logging

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

    def load_images_main_loop(self, folder_path: str):
        # load the images folder and loop over them, for each image extract text and metadata using tools defined in classes.
        metadata_extractor = MetadataExtractor()
        ocr_engine = OCREngine()

        images_handled_successfully = 0
        images_directory = IngestionConfig.images_folder_path
        for image in images_directory.rglob("*"):
            if not image.is_file():  # Check if it is a file
                logger.error(f'{file_path} is not a file')
                continue
            try:
                image_path = str(image)
                text = ocr_engine.extract_text(image_path)
                metadata = metadata_extractor.extract_metadata(image_path)
                message = metadata.items()
                message['text'] = text
                published = producer.publish(message=message)
                throw_exceptions('publish message', published)
                binary_image = metadata_extractor.get_binary_content(image_path)
                sent = client.save_binary_image(content=binary_image)
                throw_exceptions('send content to mongodb service', sent)

            except Exception as e:
                logger.error(e)

        return {
            'images handled successfully': images_handled_successfully
        }


main_config = IngestionConfig() #TODO: fill this up

orchestrator = IngestionOrchestrator() #TODO: fill this up