from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton


def generate_main_menu():
    builder = ReplyKeyboardBuilder()

    builder.row(
        KeyboardButton(text="📝 Barcha kategoriyalar"),
    )
    builder.row(
        KeyboardButton(text="🛒 Savatcha"),
        KeyboardButton(text="📄 Buyurtmalar tarixi"),
    )
    builder.row(
        KeyboardButton(text="⚙️ Sozlamalar"),
        KeyboardButton(text="📍 Filiallar", request_location=True),
    )

    return builder.as_markup(resize_keyboard=True)
