from aiogram.utils.keyboard import InlineKeyboardBuilder


def generate_cart_menu():
    builder = InlineKeyboardBuilder()

    builder.button(text="❌ Savatchamni tozalab yuborish",
                   callback_data="clear-cart")
    builder.button(text="💳 To'lov uchun davom etish", callback_data="pay")
    builder.adjust(1)
    
    return builder.as_markup()
