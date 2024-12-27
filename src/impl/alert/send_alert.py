from src.impl.bot import send_message as bot_send_impl
import logging

async def send_alert_to_telegram(chat_id: int, message: str) -> bool:
    """
    Handles the logic of sending an alert.

    Args:
        chat_id (int): The Telegram chat ID to send the alert to.
        message (str): The alert message content.

    Returns:
        bool: True if the alert was sent successfully, False otherwise.
    """
    try:
        success = await bot_send_impl.send_message(chat_id, message)

        if success:
            logging.info(f"Alert sent successfully: chat_id={chat_id}, message='{message}'")
        else:
            logging.error(f"Failed to send alert: chat_id={chat_id}, message='{message}'")

        return success
    except Exception as e:
        logging.error(f"Error in send_alert logic: {e}")
        return False