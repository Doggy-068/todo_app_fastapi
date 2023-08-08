from pydantic import BaseModel


class UploadFileReturn(BaseModel):
    file_url: str
