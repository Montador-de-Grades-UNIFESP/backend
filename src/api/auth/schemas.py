from pydantic import BaseModel

class SessaoPost(BaseModel):
    id_token: str
