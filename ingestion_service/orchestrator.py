class IngestionConfig:
    pass


class IngestionOrchestrator:
    """
    manger the service:
    GET request is a trigger, images folder load into the system,
    for each image: metadata and text extracted from the image.
    send each one to Kafka via producer, and save binary image in MongoDB.
    """