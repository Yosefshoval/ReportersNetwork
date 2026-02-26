import os

class IndexerConfig:
    kafka_url = os.getenv('KAFKA_URL')
    kafka_topics = [
        os.getenv('KAFKA_RAW_TOPIC'),
        os.getenv('KAFKA_CLEAN_TOPIC'),
        os.getenv('KAFKA_ANALYTIC_TOPIC')
    ]

    consumer_config = {
        "bootstrap.servers": kafka_url,
        "group.id": "elastic_team",
        "auto.offset.reset": "earliest"
    }

    producer_config = {
        "bootstrap.servers": kafka_url
    }

    elastic_url = os.getenv('ELASTIC_URL')
    elastic_index = os.getenv('ELASTIC_INDEX')
