import os

import qrcode
from aiogram import types

from loader import dp


@dp.message_handler(content_types=['text'])
async def echo_text_message(message: types.Message):
    img = qrcode.make(message.text)
    img.save(os.path.join('temp', f'{message.from_user.id}.png'))
    await message.answer_photo(types.InputFile(os.path.join('temp', f'{message.from_user.id}.png')))
    os.remove(os.path.join('temp', f'{message.from_user.id}.png'))
