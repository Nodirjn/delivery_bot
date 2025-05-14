from aiogram.types import CallbackQuery
from aiogram import F

from router import router
from loader import db
from keyboards.inline.product import generate_product_menu


@router.callback_query(lambda call: "product" == call.data.split(":")[0])
async def product(call: CallbackQuery):
    product_id = int(call.data.split(":")[-1])
    
    product = db.get_product(product_id=product_id)
    price = f"{product.get('price'):,.2f}".replace(",", " ")
    caption = f"""
Product: <b>{product.get('name')}</b>

About: <b>{product.get('description')}</b>

Price: <b>{price} so'm</b>
"""

    await call.message.delete()
    await call.message.answer_photo(
        photo=product.get('photo'),
        caption=caption,
        reply_markup=generate_product_menu(category_id=product.get('category_id'),
                                           product_id=product.get('id')),
        parse_mode="HTML",
    )

