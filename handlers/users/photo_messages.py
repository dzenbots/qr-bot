import os

from aiogram.types import Message

from loader import dp
from utils import QRReader


@dp.message_handler(content_types=['photo'])
async def photo_message(message: Message):
    await message.photo[-1].download(os.path.join('temp', f'{message.chat.id}.jpg'))
    qr = QRReader(filename=os.path.join('temp', f'{message.chat.id}.jpg'))
    await message.answer(text=f'В QR-коде закодированы следующие данные:\n\n{qr.picture_qr_reader()}')
    os.remove(os.path.join('temp', f'{message.chat.id}.jpg'))
