from aiogram.types import CallbackQuery
from aiogram import F

from router import router
from loader import db


@router.callback_query(F.data == "clear-cart")
async def clear_cart(call: CallbackQuery):
    user_id = db.get_user(telegram_id=call.from_user.id).get('id')
    db.clear_user_cart(user_id=user_id)
    
    await call.message.delete()
    await call.answer(text="Savatchangiz tozalandi ✅", show_alert=True)
