from aiogram.types import Message
from aiogram import F

from router import router
from keyboards.reply.main_menu import generate_main_menu


@router.message(F.text == "👈 Bosh menyu")
async def back(message: Message):
    await message.answer(text="Harakatni tanlang",
                         reply_markup=generate_main_menu())
