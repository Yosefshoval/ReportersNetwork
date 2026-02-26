from pydantic import BaseModel

class Request(BaseModel):
    image_id: str
    image_name: str
