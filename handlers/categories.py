from aiogram.types import Message
from aiogram import F

from router import router
from keyboards.inline.categories import generate_categories_table


@router.message(F.text == "📝 Barcha kategoriyalar")
async def categories(message: Message):
    await message.answer(text="Harakatni tanlang",
                         reply_markup=generate_categories_table())
