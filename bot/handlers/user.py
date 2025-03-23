from aiogram import Router, Bot
from aiogram.types import ChatMemberUpdated

from bot.texts import WELCOME_MESSAGE

user_router = Router()


@user_router.chat_member()
async def on_user_join(event: ChatMemberUpdated, bot: Bot):
    if event.old_chat_member.status in {"left", "kicked"} and event.new_chat_member.status == "member":
        user = event.new_chat_member.user
        await bot.send_message(
            chat_id=event.chat.id,
            text=WELCOME_MESSAGE.format(tg_name=user.username, full_name=user.full_name)
        )
