import easyocr
import subprocess
from PIL import Image
import os
# from orchestrator import logger


class OCREngine:
    """
    principle to extract full text found in the image. return only text field.
    """
    def __init__(self):
        self.reader = easyocr.Reader(['en'])

    def extract_text(self, image_path):
        result = self.reader.readtext(image_path, detail=0, paragraph=True)
        # logger.info(f'text from image {image_path} extracted.')
        print(f'text from image {image_path} extracted.')
        return result


class MetadataExtractor:
    """
    principle to extract metadata from the image:
    - file_size_byts (int)
    - width (int)
    - height (int)
    """

    @staticmethod
    def extract_metadata(image_path: str):
        with Image.open(image_path) as img:
            width, height = img.size
            image_format = img.format

            metadata = {
                "width": width,
                "height": height,
                "format": image_format,
                'file_size': os.path.getsize(image_path)
            }
            # logger.info(f'metadata from image {image_path} extracted.')
            print(f'metadata from image {image_path} extracted.')
            return metadata

    @staticmethod
    def get_binary_content(image_path: str):
        """
        :param image_path:
        :return: binary content of image
        """
        with open(image_path, 'rb') as file:
            binary_image = file.read()
        # logger.info('catch binary image')
        print('catch binary image')
        return binary_image
