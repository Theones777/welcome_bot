import asyncio
import shutil
from datetime import datetime, time, timedelta

from aiogram import Bot

from bot.clients.init_clients import pyro_client
from bot.log import logger
from config import Config


async def check_new_post(bot: Bot):
    status = "None"
    while True:
        now = datetime.now()
        target_time = time(Config.REMIND_TIME, Config.REMIND_MINUTES)

        if now.time() > target_time:
            next_run = datetime.combine(now.date(), target_time) + timedelta(days=1)
        else:
            next_run = datetime.combine(now.date(), target_time)

        wait_seconds = (next_run - now).total_seconds()
        await asyncio.sleep(wait_seconds)
        if post_info := await pyro_client.get_new_post():
            post, caption = post_info
            await bot.send_photo(Config.TARGET_CHAT_ID, photo=post, caption=caption)
            status = "SUCCESS"
            shutil.rmtree("downloads")
        logger.info(f"Check new post - {status}")
