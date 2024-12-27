from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.impl.alert.send_alert import send_alert_to_telegram

router = APIRouter()

class AlertRequest(BaseModel):
    chat_id: int
    message: str

@router.post("/alert")
async def alert(data: AlertRequest):
    """
    Forward an alert message to the Telegram bot.
    """
    success = await send_alert_to_telegram(data.chat_id, data.message)
    if not success:
        raise HTTPException(status_code=500, detail="Failed to send alert.")
    return {"ok": True}