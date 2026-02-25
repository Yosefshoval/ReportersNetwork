from consumer import KafkaConsumer
from producer import KafkaPublisher
from cleaning import TextCleaner
from logging import Logger


class CleanOrchestrator:
    def __init__(self, logger: Logger):
        self.logger = logger
        self.consumer = KafkaConsumer(logger)
        self.publisher = KafkaPublisher(logger)

    def main_loop(self):
        while True:
            try:
                message = self.consumer.get_images_data()
                if message is None:
                    continue

                self.logger.info(f'image data received from kafka. image id: {message['image_id']}')

                # clean text
                text = message.get('text')
                cleaned_text = TextCleaner(self.logger).clean_text(text)
                message['cleaned_text'] = cleaned_text

                # publish
                self.publisher.publish_cleaned_text(
                    message=message
                )

            except Exception as e:
                self.logger.error(e)