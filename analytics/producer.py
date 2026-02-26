from logging import Logger
from confluent_kafka import Producer
from config import AnalyticsConfig
import json


class KafkaPublisher:
    def __init__(self, logger: Logger):
        self.logger = logger
        self.producer = Producer(AnalyticsConfig.producer_config)
        self.logger.info('producer created')

    def publish(self, message: dict):
        self.producer.produce(
            topic=AnalyticsConfig.kafka_produce_topic,
            value=json.dumps(message).encode()
        )

        self.producer.flush()
        self.logger.info(f'message of image {message["image_id"]} published to kafka on topic {AnalyticsConfig.kafka_produce_topic}')



