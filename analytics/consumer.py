from logging import Logger
from confluent_kafka import Consumer
from config import AnalyticsConfig
import json

class KafkaConsumer:
    def __init__(self, logger: Logger):
        self.logger = logger
        self.consumer = Consumer(AnalyticsConfig.consumer_config)
        self.consumer.subscribe([AnalyticsConfig.kafka_subscribe_topic])
        self.logger.info(f'consumer created and subscribe to topic {self.consumer.list_topics(AnalyticsConfig.kafka_subscribe_topic)}')


    def get_images_data(self):
        image = self.consumer.poll(1.0)
        if image is None:
            self.logger.info('message is None')
            return None
        if image.error():
            self.logger.error(image.error())

        image_value = json.loads(image.value().decode('utf-8'))
        self.logger.info(f'message received: {image_value["image_id"]}')
        return image_value
