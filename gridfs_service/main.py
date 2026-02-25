from fastapi import FastAPI
from config import Config
from schema import Request
from mongodb import MongoOperations

logger = Config.logger

client = MongoOperations()
logger.info(f'mongodb connected. {client.client.is_mongos}')

app = FastAPI()
logger.info('server created')


@app.get('/health')
def health_check():
    return {"status": "healthy"}


@app.post('/insert_image')
def insert_image(image: Request):
    try:
        inserted = client.insert_bin_image(
            binary_image=image.content,
            image_id=image.image_id,
            image_name=image.image_name
        )
        message = f'image with id {image.image_id} inserted: {inserted}'
        logger.info(message)
        return {f'image with id {image.image_id} inserted: {inserted}'}
    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    uvicorn.run(
        app='main:app',
        host='0.0.0.0',
        port=int(Config.server_port)
    )
    logger.info('server running')