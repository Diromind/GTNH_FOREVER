import os
import json


def read_token_from_file(token_path: str) -> str:
    if not os.path.exists(token_path):
        raise FileNotFoundError(f"Token file '{token_path}' not found.")

    with open(token_path, "r") as file:
        token = file.read().strip()

    if not token:
        raise ValueError(f"Token file '{token_path}' is empty.")

    return token

def load_config(config_path: str) -> dict:
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file '{config_path}' not found.")

    # Load JSON config
    with open(config_path, "r") as file:
        config = json.load(file)

    # Read the bot token from the token path
    token_path = config.get("token_path")
    if not token_path:
        raise ValueError("'token_path' is missing in the config file.")

    bot_token = read_token_from_file(token_path)
    config["bot_token"] = bot_token  # Add token to the config dictionary

    return config

CONFIG_PATH = "./config.json"
config = load_config(CONFIG_PATH)