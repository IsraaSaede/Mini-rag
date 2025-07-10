from fastapi import FastAPI, APIRouter ,Depends, UploadFile ,status
from fastapi.responses import JSONResponse
from models import ResponseSignal   
from helpers.config import get_settings ,Settings
import os
import aiofiles
import logging
from controllers import DataController,ProjectController ,processController
from .schemes.data import ProcessRequest


logger = logging.getLogger('uvicorn.error')
data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"],
    responses={404: {"description": "Not found"}},
)
@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile, 
                      app_settings: Settings = Depends(get_settings)):
        data_controller = DataController()
        is_valid , result_signal = data_controller.validate_uploaded_file(file=file)# validate file type and size

        if not is_valid:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"message": result_signal}
            )
        
        project_dir_path = ProjectController().get_project_path(project_id=project_id)
        file_path , file_id = data_controller.generate_unique_filepath(
            orf_file_name=file.filename,
            project_id=project_id
            )
        try:
            async with aiofiles.open(file_path, 'wb') as f:
                while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                    await f.write(chunk)
        except Exception as e:
            logger.error(f"Error uploading file: {e}")
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"message": ResponseSignal.FILE_UPLOADED_FAILED.value}
            )
        return JSONResponse(
                content={"message": ResponseSignal.FILE_UPLOADED_SUCCESSFULLY.value
                         , "file_id": file_id},
            )
@data_router.post("/process/{project_id}")
async def process_data(project_id: str, process_reqest: ProcessRequest):
    file_id = process_reqest.file_id
    chunk_size = process_reqest.chunk_size
    overlap_size = process_reqest.overlab_size

    process_controller = processController(project_id=project_id)

    file_content = process_controller.get_file_content(file_id=file_id)

    file_chunks = process_controller.process_file_content(
        file_content=file_content,
        file_id=file_id,
        chunk_size=chunk_size,
        overlap_size=overlap_size
        )

    if file_chunks is None or len(file_chunks) == 0:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"signal": ResponseSignal.PROCESSING_FAILED.value}
        )
    return file_chunks



