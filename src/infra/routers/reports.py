from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_report_stub():
    return {"message": "Report generation stub"}
