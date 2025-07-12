from enum import Enum

class ProcessingEnum(str, Enum):

    TEXT = "txt"
    PDF = "pdf"
    DOCX = "docx"
    CSV = "csv"