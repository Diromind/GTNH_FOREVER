from aiogram import Bot
import logging

from src.impl.config.config import config

BOT = Bot(token=config["bot_token"])

async def send_message(chat_id: int, message: str) -> bool:
    """
    Sends a message to a Telegram chat using the bot.

    Args:
        chat_id (int): The Telegram chat ID.
        message (str): The message to send.

    Returns:
        bool: True if the message was sent successfully, False otherwise.
    """
    try:
        await BOT.send_message(chat_id=chat_id, text=message)

        await BOT.session.close()
        return True
    except Exception as e:
        logging.error(f"Failed to send message to Telegram. Error: {e}")
        return False