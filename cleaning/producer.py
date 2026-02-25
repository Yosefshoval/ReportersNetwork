from logging import Logger
from confluent_kafka import Producer
from config import CleanConfig
import json


class KafkaPublisher:
    def __init__(self, logger: Logger):
        self.logger = logger
        self.producer = Producer(CleanConfig.producer_config)
        self.logger.info('producer created')


    def publish_cleaned_text(self, message: dict):

        self.producer.produce(
            topic=CleanConfig.kafka_produce_topic,
            value=json.dumps(message).encode()
        )

        self.producer.flush()
        self.logger.info(f'message {message} published to kafka on topic {CleanConfig.kafka_produce_topic}')
