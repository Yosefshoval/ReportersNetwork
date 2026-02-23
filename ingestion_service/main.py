from fastapi import FastAPI
import logging

logger = logging.getLogger('Ingestion service')

app = FastAPI()

@app.get('/images_loader')
def load_images():
    pass

