import easyocr
import subprocess

images_folder_path = '../images/tweet_images'


class OCREngine:
    """
    principle to extract full text found in the image. return only text field.
    """
    def __init__(self):
        self.reader = easyocr.Reader(['en'])

    def extract_text(self, image_path: str):
        result = self.readtext(image_path, detail=0, paragraph=True)
        return result


class MetadataExtractor:
    """
    principle to extract metadata from the image:
    - file_size_byts (int)
    - width (int)
    - height (int)
    """
    def __init__(self):
        self.exeProcess = "hachoir-metadata"

    def extract_metadata(self, image_path: str):
        process = subprocess.Popen([self.exeProcess, image_path],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT,
                                   universal_newlines=True)
        Dic = {}

        for tag in process.stdout:
            line = tag.strip().split(':')
            Dic[line[0].strip()] = line[-1].strip()

        for k, v in Dic.items():
            print(k, ':', v)
        return Dic


    def get_binary_content(self, image):
        pass