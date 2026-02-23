from confluent_kafka import Producer


class KafkaPublisher:
    """
    Principle to publish extracted text and metadata about the image to topic RAW in Kafka.
    """
    def publish(self, message: dict):
        pass

producer = KafkaPublisher()