import nltk
from nltk.corpus import stopwords
import re
from config import CleanConfig


nltk.download('stopwords')
stop_words = set(stopwords.words('english'))


class TextCleaner:

    @staticmethod
    def clean_text(text: str):
        cleaned_string = ''.join(c for c in text.lower() if c.islower() or c == ' ' or c.isdigit())
        words = cleaned_string.split()
        cleaned_words = [w for w in words if w not in stop_words]
        return " ".join(cleaned_words)

