from pydantic import BaseModel

class Request(BaseModel):
    content: str
    image_id: str
    image_name: str
