import asyncio

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from bot.clients.init_clients import bot, pyro_client
from bot.handlers.user import user_router
from bot.log import logger
from bot.utils import check_new_post


async def main():
    # bot init
    logger.info("Bot init...")
    dp = Dispatcher(storage=MemoryStorage())

    # include routers
    dp.include_router(user_router)

    # bot start
    await bot.delete_webhook(drop_pending_updates=True)

    await pyro_client.client.start()
    asyncio.create_task(check_new_post(bot))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
