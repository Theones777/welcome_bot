from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config:
    BOT_TOKEN = getenv("BOT_TOKEN")
    TARGET_CHAT_ID = getenv("TARGET_CHAT_ID")
    CHANNEL_ID = getenv("CHANNEL_ID")

    API_ID = getenv("API_ID")
    API_HASH = getenv("API_HASH")
    SESSION_STRING = getenv("SESSION_STRING")
    TG_SESSION_NAME = "my_session"
