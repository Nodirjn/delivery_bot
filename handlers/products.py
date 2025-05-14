from aiogram.types import CallbackQuery
from aiogram import F

from router import router
from keyboards.inline.products import generate_products_table


@router.callback_query(lambda call: "category" in call.data)
async def products(call: CallbackQuery):
    category_id = int(call.data.split(":")[-1])   # "category:1".split(":")[-1] => ["category", "1"]
    
    await call.message.edit_reply_markup(
        reply_markup=generate_products_table(category_id=category_id)
    )


