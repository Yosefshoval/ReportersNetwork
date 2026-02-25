from confluent_kafka import Consumer
from config import CleanConfig

logger = CleanConfig.logger


class KafkaConsumer:
    def __init__(self):
        self.consumer = Consumer(CleanConfig.consumer_config)
        logger.info('consumer created')
        self.consumer.subscribe([CleanConfig.kafka_subscribe_topic])

    def get_images_data(self):
        while True:
            image = self.consumer.poll(1.0)

