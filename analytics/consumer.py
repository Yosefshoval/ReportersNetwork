from logging import Logger
from confluent_kafka import Consumer

class KafkaConsumer:
    def __init__(self, logger: Logger):
        self.logger = logger

