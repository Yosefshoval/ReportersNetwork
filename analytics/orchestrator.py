from logging import Logger
from consumer import KafkaConsumer
from producer import KafkaPublisher
from analyzer import TextAnalyzer


class AnalyticsOrchestrator:
    def __init__(self, logger: Logger):
        self.logger = logger
        self.consumer = KafkaConsumer(logger)
        self.producer = KafkaPublisher(logger)
        self.analyzer = TextAnalyzer(logger)


    def run(self):
        self.logger.info('loop starting')
        while True:
            try:
                message = self.consumer.get_images_data()
                if not message:
                    continue

                text = message['cleaned_text']

                top_words = self.analyzer.top_ten_words(text)
                weapons = self.analyzer.find_weapons(text)
                sentiment = self.analyzer.sentiment_analytics(text)

                updated_message = {'top_words' : top_words, 'weapons' : weapons, 'sentiment' : sentiment} | message
                self.producer.publish(updated_message)

            except Exception as e:
                self.logger.error(e)