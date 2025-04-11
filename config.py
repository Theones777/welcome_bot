from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config:
    BOT_TOKEN = getenv("BOT_TOKEN")
    POST_TARGET_CHAT_ID = getenv("POST_TARGET_CHAT_ID")
    WELCOME_TARGET_CHAT_ID = getenv("WELCOME_TARGET_CHAT_ID")
    CHANNEL_ID = getenv("CHANNEL_ID")

    SESSION_STRING = getenv("SESSION_STRING")
    TG_SESSION_NAME = "my_account"
    CHANNEL_TAG = "#ДмитрийТроцкий_цитата"
    REMIND_TIME = int(getenv("REMIND_TIME", 3))
    REMIND_MINUTES = int(getenv("REMIND_MINUTES", 0))
