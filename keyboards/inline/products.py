from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

from loader import db


def generate_products_table(category_id):
    products = db.get_products(category_id=category_id)
    builder = InlineKeyboardBuilder()

    for product in products:
        builder.button(text=product.get("name"), callback_data=f"product:{product.get('id')}")

    builder.adjust(2)
    builder.row(
        InlineKeyboardButton(text="👈 Orqaga", callback_data="back_to_categories")
    )
    return builder.as_markup()
