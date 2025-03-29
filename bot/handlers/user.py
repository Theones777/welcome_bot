from aiogram import Router, Bot
from aiogram.filters import CommandStart
from aiogram.types import ChatMemberUpdated, Message
from pyrogram import filters

from bot.clients.init_clients import pyro_client, bot
from bot.log import logger
from bot.texts import WELCOME_MESSAGE
from config import Config

user_router = Router()



@user_router.chat_member()
async def on_user_join(event: ChatMemberUpdated, bot: Bot):
    if event.old_chat_member.status in {"left", "kicked"} and event.new_chat_member.status == "member":
        user = event.new_chat_member.user
        await bot.send_message(
            chat_id=event.chat.id,
            text=WELCOME_MESSAGE.format(tg_name=user.username, full_name=user.full_name)
        )


@pyro_client.client.on_message(filters.channel)
async def handle_channel_post(message: Message):
    logger.warning(f"CHAT_ID: {message.chat.id}")
    try:
        logger.warning(f"INFO: {dict(message.chat)}")
    except:
        pass
    text = f"📢 Новый пост из {message.chat.title}:\n\n{message.text or 'Медиа/документ'}"
    await bot.send_message(Config.TARGET_CHAT_ID, text)


@user_router.message(CommandStart())
async def start_cmd(message: Message):
    user_id = message.from_user.id
    await message.answer(f"✅ Теперь вы будете получать сообщения из канала! {user_id}")
