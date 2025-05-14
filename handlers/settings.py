from aiogram import types
from aiogram import F

from router import router
from loader import db
from keyboards.reply.settings import generate_settings_menu


@router.message(F.text == "⚙️ Sozlamalar")
async def settings(message: types.Message):
    telegram_id = message.from_user.id
    await message.answer(text="Harakatni tanlang", reply_markup=generate_settings_menu(telegram_id=telegram_id))
