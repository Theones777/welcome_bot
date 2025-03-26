from pyrogram import Client
from aiogram.types import Message
import asyncio

from bot.log import logger
from config import Config


class PyroClient:
    def __init__(self):
        self.client = Client(
            Config.TG_SESSION_NAME,
            Config.API_ID,
            Config.API_HASH,
            session_string=Config.SESSION_STRING,
        )
