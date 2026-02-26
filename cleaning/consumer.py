from confluent_kafka import Consumer
from config import CleanConfig
import json
from logging import Logger


class KafkaConsumer:
    def __init__(self, logger: Logger):
        self.logger = logger
        self.consumer = Consumer(CleanConfig.consumer_config)
        self.consumer.subscribe([CleanConfig.kafka_subscribe_topic])
        self.logger.info(f'consumer created and subscribe to topic {CleanConfig.kafka_subscribe_topic}')

    def get_images_data(self):
        image = self.consumer.poll(1.0)
        if image is None:
            return None
        if image.error():
            self.logger.error(image.error())
        return json.loads(image.value().decode('utf-8'))


