from ocr import OCREngine, MetadataExtractor
from producer import producer
from sender import client
from pathlib import Path
import uuid
from config import IngestionConfig
import os




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

        IngestionConfig.logger.info('loop starting....')
        IngestionConfig.logger.info(f' images_directory.exists(): {images_directory.exists()}')
        for image in images_directory.rglob("**/*"):
            IngestionConfig.logger.info(f'current image: {image}')
            if not image.is_file():  # Check if it is a file
                IngestionConfig.logger.error(f'{image} is not a file')
                continue
            try:
                image_id = uuid.uuid4()
                IngestionConfig.logger.info('uuid created.')
                image_path = str(image)

                # 1: extract text
                text = ocr_engine.extract_text(image_path=image_path)

                # 2: extract metadata
                metadata = metadata_extractor.extract_metadata(image_path=image_path)
                metadata['image_id'] = str(image_id)

                # 3: send to mongodb
                binary_image = metadata_extractor.get_binary_content(image_path)
                sent = client.save_binary_image(binary_image, image_id, image_path)
                throw_exceptions('send content to mongodb service', sent)

                # 4: send to kafka
                full_image_data = metadata | {'text' : text}

                published = producer.publish(full_image_data)
                throw_exceptions('publish message', published)

                images_handled_successfully += 1
            except Exception as e:
                IngestionConfig.logger.error(e)
                continue

        return {
            'images handled successfully': images_handled_successfully
        }