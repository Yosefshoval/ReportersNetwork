from orchestrator import IndexOrchestrator
import logging


logger = logging.getLogger(' elastic consumer service ')
logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    logger.info('starting indexer service...')
    orchestrator = IndexOrchestrator(logger)
    orchestrator.run()
