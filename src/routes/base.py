from fastapi import FastAPI, APIRouter
 # Load environment variables from .env file
import os

base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
    responses={404: {"description": "Not found"}},
)


@base_router.get("/")
async def welcome():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return {
        "APP_NAME": app_name,
        "APP_VERSION": app_version,
    }