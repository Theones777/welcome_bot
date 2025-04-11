from datetime import datetime, timedelta

from aiogram.types import FSInputFile
from pyrogram import Client
from config import Config


class PyroClient:
    def __init__(self):
        self.client = Client(
            Config.TG_SESSION_NAME,
            session_string=Config.SESSION_STRING
        )

    async def get_new_post(self):
        post, caption = None, None
        yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
        history = self.client.get_chat_history(chat_id=Config.CHANNEL_ID, limit=5)
        async for el in history:
            post_date = el.date.strftime("%Y-%m-%d")
            if el.caption and Config.CHANNEL_TAG in el.caption and yesterday == post_date:
                photo_path = await self.client.download_media(el.photo)

                post = FSInputFile(photo_path)
                caption = el.caption
                break
        return post, caption
