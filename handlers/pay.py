from aiogram.types import (CallbackQuery,
                           LabeledPrice,
                           PreCheckoutQuery,
                           Message,
                           ShippingAddress,
                           ShippingOption,
                           ShippingQuery)
from aiogram import F

from router import router
from loader import db
from config import PAYMENT_TOKEN


@router.callback_query(F.data == "pay")
async def start_checkout(call: CallbackQuery):
    user_id = db.get_user(telegram_id=call.from_user.id).get('id')
    orders = db.get_cart_products(user_id=user_id)

    prices = []
    text = ""

    for order in orders:
        product = db.get_product(product_id=order.get('product_id'))
        prices.append(LabeledPrice(label=f"{product.get('name')}", amount=int(order.get('total_price')) * 100))
        text += f"{product.get('name')} x{order.get('quantity')}, "

    await call.message.answer_invoice(
        max_tip_amount=500000,
        suggested_tip_amounts=[100000, 300000, 500000],
        title="Savatingiz uchun hisob",
        description=text,
        currency="UZS",
        prices=prices,
        provider_token=PAYMENT_TOKEN,
        payload="{'user': 1, 'is_paid': false}",
        photo_url="https://i.pinimg.com/736x/9a/13/f7/9a13f766beb55d7c5d2ea185a4111376.jpg",
        need_shipping_address=True,
        need_email=True,
        need_name=True,
        need_phone_number=True,
        is_flexible=True,
    )


@router.pre_checkout_query()
async def pre_checkout(checkout_query: PreCheckoutQuery):
    await checkout_query.answer(ok=True)


@router.message()
async def successful_payment_handler(message: Message):
    if message.successful_payment:
        payment_info = message.successful_payment
        print(payment_info)
        await message.answer(text="To'lovingiz qabul qilindi, iltimos kuting")


@router.shipping_query()
async def send_shipping_options(shipping_query: ShippingQuery):
    shipping_options = [
        ShippingOption(id="fast-delivery", title="Tezda yetkazib berish",
                       prices=[LabeledPrice(label="Tezda yetkaizb berish", amount=5000000)]),
        ShippingOption(id="standart-delivery", title="Standart yetkazib berish",
                       prices=[LabeledPrice(label="Standart yetkaizb berish", amount=1500000)]),
    ]

    await shipping_query.answer(
        ok=True,
        shipping_options=shipping_options,
    )
