from aiogram import types
from aiogram.filters.command import CommandStart

from router import router
from loader import db
from keyboards.reply.main_menu import generate_main_menu


@router.message(CommandStart())
async def start(message: types.Message):
    telegram_id = message.from_user.id
    fullname = message.from_user.full_name
    username = message.from_user.username

    try:
        db.register_user(telegram_id, fullname, username)
        text = f"Assalomu alaykum, {fullname} 👋\n\nMuvaffaqiyatli ro'yxatga olindingiz ✅"
    except:
        text = f"Qaytganingizdan xursandmiz, {fullname} 👋"
    
    await message.answer(text=text, reply_markup=generate_main_menu())
