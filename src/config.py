from fastapi import FastAPI
from src.infra.routers.base_router import base_api_router

app = FastAPI()

app.include_router(base_api_router)
