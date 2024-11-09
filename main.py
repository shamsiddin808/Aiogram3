import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, CommandStart
import asyncio
from aiogram.types import ContentType, Message
from aiogram.types import ContentType


from aiogram import types
import re

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_TOKEN = '6560320149:AAFeQaPjUVO4i13K1ZBY1_P1m2ebn5h-Xk0'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.reply("Salom! Bu oddiy AIogram 3.x bot.")

@dp.message(F.text.regexp(r"\d+"))
async def numbers_message(message: types.Message):
    await message.reply("Bu xabar raqamlar o'z ichiga oladi.")

@dp.message()
async def echo_message(message: types.Message):
    await message.reply(message.text)


@dp.message(F.content_type == ContentType.PHOTO)
async def photo_message(message: types.Message):
    photo = message.photo[-1]
    await photo.download(destination_file="photo.png")
    await message.reply("Rasm uchun rahmat!")

@dp.message(F.content_type == ContentType.VOICE)
async def handle_voice_message(message: types.Message):
    await message.reply("Thank you for the voice message!")

@dp.message(F.chat.type == "private")
async def private_chat_message(message: types.Message):
    await message.reply("Bu xabar shaxsiy chatda yuborilgan.")

@dp.message(F.from_user.id.in_({29083453, 987654321}))
async def specific_users_message(message: types.Message):
    await message.reply("Bu xabar faqat ma'lum foydalanuvchilar uchun.")

@dp.message(F.is_forward)
async def forwarded_message_handler(message: types.Message):
    print("fdsfs")
    await message.reply("Siz forward qilingan xabar yubordingiz.")



async def main():
    try:
        print("Bot ishga tushmoqda...")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        logger.info("Bot seansi yopildi")
if __name__ == "__main__":
    asyncio.run(main())
