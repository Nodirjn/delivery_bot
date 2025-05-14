from aiogram.types import CallbackQuery
from aiogram import F

from loader import db
from router import router
from keyboards.inline.product import generate_product_menu


@router.callback_query(lambda call: "product-action" == call.data.split(":")[0])
async def product_action(call: CallbackQuery):
    action = call.data.split(":")[1]
    quantity = int(call.data.split(":")[2])
    product_id = call.data.split(":")[3]
    product = db.get_product(product_id)

    if action == "increment":
        quantity += 1
    elif action == "decrement":
        if quantity > 1:
            quantity -= 1

    price = f"{(product.get('price') * quantity):,.2f}".replace(",", " ")
    caption = f"""
Product: <b>{product.get('name')}</b>

About: <b>{product.get('description')}</b>

Price: <b>{price} so'm</b>
"""

    await call.message.edit_caption(
        caption=caption,
        reply_markup=generate_product_menu(
            category_id=product.get('category_id'),
            product_id=product.get('id'),
            quantity=quantity),
            parse_mode="HTML"
    )
