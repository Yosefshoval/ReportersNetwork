from logging import Logger


class KafkaConsumer:
    def __init__(self, logger: Logger):
        self.logger = logger

