from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")
    await message.answer(
        text=f'Отправь мне фото QR-кода для получения закодированной в нем информации. Или пришли мне текстовое сообщение, которое я закодирую в QR-код!')
