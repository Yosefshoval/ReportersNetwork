from fastapi import FastAPI, UploadFile, File, Form
from config import Config
from schema import Request
from mongodb import MongoOperations
import logging

logger = logging.getLogger('gridfs service')
logging.basicConfig(level=logging.INFO)


client = MongoOperations(logger)
logger.info(f'mongodb connected: {client.client.is_mongos}')

app = FastAPI()
@app.post('/insert_image')
def insert_image(image_id: str = Form(...), file: UploadFile = File(...)):
    try:
        image_byts = file.file
        filename = file.filename

        inserted = client.insert_bin_image(
            binary_image=image_byts,
            image_id=image_id,
            image_name=filename
        )

        message = f'image with id {image_id} inserted: {inserted}'
        logger.info(message)
        return {'message' : f'image with id {image_id} inserted: {inserted}'}
    except Exception as e:
        logger.error(e)


logger.info('server created')


@app.get('/health')
def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    uvicorn.run(
        app='main:app',
        host='0.0.0.0',
        port=int(Config.server_port)
    )
    logger.info('server running')