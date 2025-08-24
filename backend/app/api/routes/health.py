from fastapi import APIRouter

router = APIRouter()

@router.get("/healthz")
async def health() -> dict:
    return {"status": "ok"}