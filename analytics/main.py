import logging
from orchestrator import AnalyticsOrchestrator

logger = logging.getLogger('analytics service')


if __name__ == "__main__":
    orchestrator = AnalyticsOrchestrator(logger)
