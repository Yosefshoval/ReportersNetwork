from orchestrator import CleanOrchestrator
import logging

logger = logging.getLogger('cleaner service')
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logger.info('starting service')
    orchestrator = CleanOrchestrator(logger)
    orchestrator.main_loop()