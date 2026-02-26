from logging import Logger
from collections import Counter


class TextAnalyzer:
    def __init__(self, logger: Logger):
        self.logger = logger


    def top_ten_words(self, text: str):

        split_it = text.split()
        counters_found = Counter(split_it)
        most_occur = counters_found.most_common(10)
        self.logger.info('text analyzed')
        return most_occur

