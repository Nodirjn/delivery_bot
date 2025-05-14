from aiogram.utils.keyboard import InlineKeyboardBuilder

from loader import db


def generate_categories_table():
    categories = db.get_categories()
    builder = InlineKeyboardBuilder()

    for category in categories:
        builder.button(text=category.get("name"), callback_data=f"category:{category.get('id')}")

    builder.adjust(2)
    return builder.as_markup()
