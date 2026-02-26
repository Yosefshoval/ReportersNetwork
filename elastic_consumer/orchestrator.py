from logging import Logger
from elastic_client import ElasticsearchClient
from consumer import KafkaConsumer
import json


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

                # serializing "top_words" if exists
                if document.get("top_words"):
                    document["top_words"] = json.dumps(document["top_words"])
                    self.logger.info('document["top_words"] serialized.')

                inserted = self.es_client.upsert(document, document.get('image_id'))
                self.logger.info(f'{inserted["result"]} in Elasticsearch: {inserted}')
                # x = {'_index': 'report_images_text', '_id': '58ea4ac0-071d-4610-87d5-2fc1f165ad51', '_version': 2, 'result': 'updated',
                # '_shards': {'total': 2, 'successful': 1, 'failed': 0}, '_seq_no': 250, '_primary_term': 1}
            except Exception as e:
                self.logger.error(e)
                continue
