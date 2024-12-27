from fastapi import APIRouter
from src.impl.alive.ping import is_alive

router = APIRouter()

@router.get("/alive")
async def alive() -> dict:
    """
    Health check endpoint to verify if the API is running.
    """
    return is_alive()