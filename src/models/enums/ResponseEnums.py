from enum import Enum


class ResponseSignal(Enum):
    FILY_TYPE_NOT_SUPPORTED = "Fily type not supported"
    FILE_SIZE_EXCEEDED = "File size exceeded"
    FILE_UPLOADED_SUCCESSFULLY = "File uploaded successfully"
    FILE_VALIDATION_FAILED = "File validation failed"
    FILE_VALIDATION_SUCCESS = "File validation successful"
    FILE_NOT_FOUND = "File not found"
    FILE_UPLOADED_FAILED = "File upload failed"
