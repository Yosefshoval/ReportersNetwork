import logging
from orchestrator import AnalyticsOrchestrator

logger = logging.getLogger('analytics service')
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    orchestrator = AnalyticsOrchestrator(logger)
    logger.info('service starting...')
    orchestrator.run()
