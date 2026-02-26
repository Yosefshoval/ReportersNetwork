from logging import Logger
from collections import Counter
from config import AnalyticsConfig
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')


class TextAnalyzer:
    def __init__(self, logger: Logger):
        self.logger = logger
        with open(AnalyticsConfig.weapons_file_path, 'r') as weapon_list:
            self.weapons_list = weapon_list.read().split()


    def top_ten_words(self, text: str):

        split_it = text.split()
        counters_found = Counter(split_it)
        most_occur = counters_found.most_common(10)
        self.logger.info('text analyzed')
        return most_occur

    def find_weapons(self, text: str):
        weapons = set()

        for word in text:
            if word in self.weapons_list:
                weapons.add(word)

        self.logger.info(f'found {len(weapons)} weapons in the text')
        return list(weapons)


    def sentiment_analytics(self, text: str):
        score = SentimentIntensityAnalyzer().polarity_scores(text)
        compound = score['compound']

        state = ''
        if  1.000 >= compound >= 0.5000:
            state = 'positive'
        elif 0.4999 >= compound >= (-0.4991):
            state = 'neutral'
        elif  (-0.4999) >= compound >= (-1.000):
            state = 'negative'

        self.logger.info(f'text score analyzed. score: {compound}.')

        return state
