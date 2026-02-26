import os

class AnalyticsConfig:
    kafka_url = os.getenv('KAFKA_URL')
    kafka_subscribe_topic = os.getenv('KAFKA_SUBSCRIBE_TOPIC')
    kafka_produce_topic = os.getenv('KAFKA_PRODUCE_TOPIC')
