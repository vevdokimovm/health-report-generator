from fastapi import APIRouter

from src.infra.routers.reports import router as reports_router

base_api_router = APIRouter(prefix="/api")

base_api_router.include_router(reports_router, prefix="/reports")