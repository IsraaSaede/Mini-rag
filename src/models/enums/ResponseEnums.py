from enum import Enum


class ResponseSignal(Enum):
    FILE_TYPE_NOT_SUPPORTED = "File type not supported"
    FILE_SIZE_EXCEEDED = "File size exceeded"
    FILE_UPLOADED_SUCCESSFULLY = "File uploaded successfully"
    FILE_VALIDATION_FAILED = "File validation failed"
    FILE_VALIDATION_SUCCESS = "File validation successful"
    FILE_NOT_FOUND = "File not found"
    FILE_UPLOADED_FAILED = "File upload failed"
    PROCESSING_FAILED = "File processing failed"
    FILE_PROCESSING_SUCCESS = "File processing successful"
