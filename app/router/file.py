from fastapi import APIRouter, Depends, UploadFile
from .auth import verify_token
from app.schema.file import UploadFileReturn

router = APIRouter(prefix='/api/file', tags=['file'], dependencies=[Depends(verify_token)])


@router.post('/upload', response_model=UploadFileReturn)
async def upload_file(file: UploadFile):
    with open(f'./file/{file.filename}', 'wb') as f:
        f.write(await file.read())
    return {
        'file_url': f'http://localhost:8000/file/{file.filename}'
    }
