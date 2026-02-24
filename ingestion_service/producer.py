from confluent_kafka import Producer
from config import IngestionConfig
import json


class KafkaPublisher:
    """
    Principle to publish extracted text and metadata about the image to topic RAW in Kafka.
    """
    def __init__(self):
        producer_config = {
            "bootstrap.servers": IngestionConfig.kafka_url
        }
        self.producer = Producer(producer_config)

    @staticmethod
    def report_status(err, msg):
        if err:
            IngestionConfig.logger.error(err)
        else:
            IngestionConfig.logger.info(msg)


    def publish(self, message: dict):
        """
        :param message:
        :return: True if sent successfully, False if not.
        """
        value = json.dumps(message).encode("utf-8")
        IngestionConfig.logger.info(f'message value: {value}')
        self.producer.produce(
            topic=IngestionConfig.kafka_topic,
            value=value,
            callback=KafkaPublisher.report_status
        )
        return True


producer = KafkaPublisher()