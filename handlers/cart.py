from aiogram.types import Message
from aiogram import F

from router import router
from loader import db
from keyboards.inline.cart import generate_cart_menu


@router.message(F.text == "🛒 Savatcha")
async def show_cart(message: Message):
    user_id = db.get_user(telegram_id=message.from_user.id).get('id')
    orders = db.get_cart_products(user_id=user_id)

    text = "🛒 Sizning savatchangiz:\n\n"
    final_price = 0
    
    for counter, order in enumerate(orders, start=1):
        product = db.get_product(product_id=order.get('product_id'))
        total_price = f"{order.get('total_price'):,.2f}".replace(",", " ")
        final_price += order.get('total_price')

        text += f"{counter}) {'-' * 10}\n"
        text += f"Maxsulot nomi: <b>{product.get('name')}</b>\n"
        text += f"Soni: <b>{order.get('quantity')} ta</b>\n"
        text += f"Umumiy narxi: <b>{total_price} so'm</b>\n\n"

    final_price = f"{final_price:,.2f}".replace(",", " ")
    text += f"Umumiy narx: <b>{final_price} so'm</b>"

    if len(orders) > 0:
        await message.answer(text=text, 
                            parse_mode="HTML", 
                            reply_markup=generate_cart_menu())
    else:
        await message.answer(text="Savatcangiz bo'sh 😐")
