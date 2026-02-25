from confluent_kafka import Producer
from config import CleanConfig
import json

logger = CleanConfig.logger

class KafkaPublisher:
    def __init__(self):
        self.producer = Producer(CleanConfig.producer_config)

    def publish_cleaned_text(self, message: dict):

        self.producer.produce(
            topic=CleanConfig.kafka_produce_topic,
            value=json.dumps(message).encode()
        )

        self.producer.flush()
        logger.info(f'message {message} published to kafka on topic {CleanConfig.kafka_produce_topic}')
