from fastapi import FastAPI
import uvicorn
from orchestrator import IngestionOrchestrator
from config import IngestionConfig
from os import getenv

app = FastAPI()

@app.get('/')
def home():
    IngestionConfig.logger.info('Home route clicked. service healthy.')
    return {
        'message' : 'server is running'
    }


@app.get('/images_loader')
def load_images():
    result = IngestionOrchestrator.load_images_main_loop()
    return result



if __name__ == "__main__":
    uvicorn.run(
        app='main:app',
        host='0.0.0.0',
        port=int(IngestionConfig.server_port)
    )
    IngestionConfig.logger.info('server started')