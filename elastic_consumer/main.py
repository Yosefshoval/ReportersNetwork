from orchestrator import IndexOrchestrator
import logging


logger = logging.getLogger('gridfs service')
logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    logger.info('starting indexer service...')
    orchestrator = IndexOrchestrator(logger)
