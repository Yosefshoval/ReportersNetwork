from elasticsearch import Elasticsearch
from config import IndexerConfig
from logging import Logger

class ElasticsearchClient:
    def __init__(self, logger: Logger):
        self.logger = logger
        self.elastic_client = Elasticsearch(IndexerConfig.elastic_url)
        self.index = IndexerConfig.elastic_index

    def upsert(self, document: dict, image_id: str):
        response = self.elastic_client.update(
            index=self.index,
            id=image_id,
            doc=document,
            doc_as_upsert=True
        )
        return response

    def search(self, query: dict):
        response = self.elastic_client.search(
            index=self.index,
            query=query
        )

        return response