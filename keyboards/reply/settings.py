from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

from loader import db

def generate_settings_menu(telegram_id):
    builder = ReplyKeyboardBuilder()
    user = db.get_user(telegram_id=telegram_id)
    is_subscribed = user.get("is_subscribed") == 1

    builder.row(
        KeyboardButton(text=f"Obunani {'ochirish' if is_subscribed else 'yoqish'}"),
        KeyboardButton(text="Manzilni kiritish"),
    )
    builder.row(
        KeyboardButton(text="👈 Bosh menyu")
    )

    return builder.as_markup(resize_keyboard=True)
