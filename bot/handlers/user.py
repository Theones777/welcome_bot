from aiogram import Router, Bot
from aiogram.filters import CommandStart
from aiogram.types import ChatMemberUpdated, Message

from bot.texts import WELCOME_MESSAGE
from config import Config

user_router = Router()



@user_router.chat_member()
async def on_user_join(event: ChatMemberUpdated, bot: Bot):
    if event.old_chat_member.status in {"left", "kicked"} and event.new_chat_member.status == "member":
        user = event.new_chat_member.user
        await bot.send_message(
            chat_id=Config.WELCOME_TARGET_CHAT_ID,
            text=WELCOME_MESSAGE.format(tg_name=user.username, full_name=user.full_name)
        )


# @user_router.message(CommandStart())
# async def start_cmd(message: Message):
#     user_id = message.from_user.id
#     await message.answer(f"✅ Теперь вы будете получать сообщения из канала! {user_id}")
