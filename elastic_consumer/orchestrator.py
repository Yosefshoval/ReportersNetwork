from logging import Logger
from elastic_client import ElasticsearchClient
from consumer import KafkaConsumer

class IndexOrchestrator:
    def __init__(self, logger: Logger):
        self.logger = logger
        self.consumer = KafkaConsumer(logger)
        self.es_client = ElasticsearchClient(logger)

    def run(self):
        self.logger.info('loop starting')
        while True:
            try:
                document = self.consumer.get_images_data()
                if document is None:
                    continue

                inserted = self.es_client.upsert(document, document.get('image_id'))
                self.logger.info(f'inserted or updated in Elasticsearch: {inserted}')

            except Exception as e:
                self.logger.error(e)
                continue
