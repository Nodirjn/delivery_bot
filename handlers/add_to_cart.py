from aiogram.types import CallbackQuery
from aiogram import F

from router import router
from loader import db


@router.callback_query(F.data.split(":")[0] == "add-to-cart")
async def cart(call: CallbackQuery):
    quantity = call.data.split(":")[1]
    product_id = call.data.split(":")[2]
    user_id = db.get_user(telegram_id=call.from_user.id).get('id')

    db.add_to_cart(user_id, product_id, quantity)
    await call.message.delete()
    await call.answer(text="Maxsulot savatchaga muvaffaqiyatli qo'shildi ✅", show_alert=True)
