import nltk
from nltk.corpus import stopwords
import re

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))


class TextCleaner:
    def __init__(self, logger):
        self.logger = logger

    def clean_text(self, text: str):
        text.replace('\n', ' ')
        cleaned_string = ''.join(c for c in text.lower() if c.islower() or c == ' ' or c.isdigit())
        words = cleaned_string.split()
        cleaned_words = [w for w in words if w not in stop_words]
        self.logger.info('text cleaned.')
        return " ".join(cleaned_words)

