from aiogram.types import CallbackQuery
from aiogram import F

from router import router
from loader import bot
from keyboards.inline.categories import generate_categories_table
from keyboards.inline.products import generate_products_table

@router.callback_query(lambda call: "back_to" in call.data)
@router.callback_query(F.data == "back_to_categories")
async def back_to_categories(call: CallbackQuery):
    if call.data.split(":")[0] == "back_to":
        category_id = call.data.split(":")[-1]
        await call.message.delete()
        await call.message.answer(
            text="Harakatni tanlang",
            reply_markup=generate_products_table(category_id=category_id)
        )
    else:
        await call.message.edit_reply_markup(
            reply_markup=generate_categories_table()
        )
