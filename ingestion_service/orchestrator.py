from ocr import OCREngine, MetadataExtractor
from main import logger
from producer import producer
from sender import client
import os

class IngestionConfig:
    IMAGES_FOLDER_PATH = os.getenv('IMAGES_FOLDER_PATH')



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
        for image in folder_path:
            try:
                text = ocr_engine.extract_text(image)
                metadata = metadata_extractor.extract_metadata(image)
                message = metadata.items()
                message['text'] = text
                published = producer.publish(message=message)
                binary_image = metadata_extractor.get_binary_content(image)
                sent = client.save_binary_image(content=binary_image)

            except Exception as e:
                logger.error(e)

        return {
            'images handled successfully': images_handled_successfully
        }


main_config = IngestionConfig() #TODO: fill this up

orchestrator = IngestionOrchestrator() #TODO: fill this up