from aiogram import Bot
import logging

import os

def read_token_from_file(bot_name: str) -> str:
    file_path = f"{bot_name}"
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Token file '{file_path}' not found.")

    with open(file_path, "r") as file:
        token = file.read().strip()
    if not token:
        raise ValueError(f"Token file '{file_path}' is empty.")

    return token

BOT_TOKEN = read_token_from_file("config.json")

BOT = Bot(token=BOT_TOKEN)

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