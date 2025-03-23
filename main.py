import asyncio

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from bot.handlers.user import user_router
from bot.log import logger
from config import Config


async def main():
    # bot init
    logger.info("Bot init...")
    dp = Dispatcher(storage=MemoryStorage())
    bot = Bot(
        token=Config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    # include routers
    dp.include_router(user_router)

    # bot start
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
