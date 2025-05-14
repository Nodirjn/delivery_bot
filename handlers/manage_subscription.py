from aiogram import types
from aiogram import F

from router import router
from loader import db
from keyboards.reply.settings import generate_settings_menu


@router.message(F.text == "Obunani o'chirish")
@router.message(F.text == "Obunani yoqish")
async def toggle_subscription_status(message: types.Message):
    telegram_id = message.from_user.id
    db.toggle_subscription_status(telegram_id)

    if message.text == "Obunani o'chirish":
        text = "❌ Obuna o'chirildi"
    else:
        text = "✅ Ubuna yondirildi"
    
    await message.answer(text=text, reply_markup=generate_settings_menu(telegram_id=telegram_id))
