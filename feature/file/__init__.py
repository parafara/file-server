from fastapi import APIRouter, UploadFile, File, Query
from fastapi.responses import FileResponse, StreamingResponse
from common.constant import FILE_SAVE_PATH

router = APIRouter(prefix="/file", tags=["file"])

@router.post("")
async def upload(uploaded_file: UploadFile = File()):
    try:
        with open(f'{FILE_SAVE_PATH}/{uploaded_file.filename}', 'xb') as file:
            file.write(await uploaded_file.read())
    except:
        return {'success': False}

    return {'success': True, 'file_id': uploaded_file.filename}

@router.get("/{file_id:str}")
async def download(file_id: str):

    return FileResponse(f'{FILE_SAVE_PATH}/{file_id}')
