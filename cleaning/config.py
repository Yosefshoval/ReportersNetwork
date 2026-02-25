import os

class CleanConfig:
    kafka_url = os.getenv('KAFKA_URL')
    kafka_subscribe_topic = os.getenv('KAFKA_SUBSCRIBE_TOPIC')
    kafka_produce_topic = os.getenv('KAFKA_PRODUCE_TOPIC')

    consumer_config = {
        "bootstrap.servers": kafka_url,
        "group.id": "cleaning_team",
        "auto.offset.reset": "earliest"
    }
    producer_config = {
        "bootstrap.servers": kafka_url
    }
