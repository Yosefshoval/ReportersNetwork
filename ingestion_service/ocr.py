import pytesseract
import subprocess
from PIL import Image
import os
from config import IngestionConfig


class OCREngine:
    """
    principle to extract full text found in the image. return only text field.
    """

    @staticmethod
    def extract_text(image_path: str):
        image = Image.open(image_path)
        result = pytesseract.image_to_string(image, lang='heb+eng')
        IngestionConfig.logger.info(f'text from image {image_path} extracted.')
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
            IngestionConfig.logger.info(f'metadata from image {image_path} extracted.')
            return metadata

    @staticmethod
    def get_binary_content(image_path: str):
        """
        :param image_path:
        :return: binary content of image
        """
        with open(image_path, 'rb') as file:
            binary_image = file.read()
        IngestionConfig.logger.info('catch binary image')
        return binary_image
