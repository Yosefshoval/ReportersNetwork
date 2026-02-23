from confluent_kafka import Producer
from orchestrator import main_config
import json


class KafkaPublisher:
    """
    Principle to publish extracted text and metadata about the image to topic RAW in Kafka.
    """
    def __init__(self):
        producer_config = {
            "bootstrap.servers": ''
        }
        self.producer = Producer(producer_config)

    @staticmethod
    def report_status(err, msg):
        if err:
            pass
        else:
            pass


    def publish(self, message: dict):
        """
        :param message:
        :return: True if sent successfully, False if not.
        """
        value = json.dumps(message).encode("utf-8")
        self.producer.produce(
            topic=main_config.kafka_topic,
            value=value,
            callback=KafkaPublisher.report_status
        )


producer = KafkaPublisher()