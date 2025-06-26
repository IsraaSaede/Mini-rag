from .BaseController import BaseController
from .ProjectController import ProjectController
from fastapi import UploadFile
import os
from helpers.config import get_settings, Settings

from models import ResponseSignal
class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale = 1024 * 1024  # 1 MB

    def validate_uploaded_file(self, file:UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False , ResponseSignal.FILY_TYPE_NOT_SUPPORTED.value
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False , ResponseSignal.FILE_SIZE_EXCEEDED.value
        
        return True , ResponseSignal.FILE_UPLOADED_SUCCESSFULLY.value
    
    def generate_unique_filename(self, orf_file_name: str , project_id: str):
        
        random_key = self.generate_unique_string()
        project_path = ProjectController().get_project_path(project_id=project_id)
        cleaned_file_name = self.get_clean_file_name(orf_file_name = orf_file_name)

        new_file_path = os.path.join(
            project_path,
            random_key + "_" + cleaned_file_name
        )
        while os.path.exists(new_file_path):
            random_key = self.generate_unique_string()
            new_file_path = os.path.join(
                project_path,
                random_key + "_" + cleaned_file_name
            )

        return new_file_path
    
    def get_clean_file_name(self, orf_file_name: str):
        # Remove any special characters and keep only alphanumeric characters and underscores
        cleaned_file_name = ''.join(c if c.isalnum() or c == '_' else '_' for c in orf_file_name)
        return cleaned_file_name
