import asyncio
import sys
import os

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from loguru import logger

logger.add('bot/logs/bot.log', format='{time:DD-MM-YY HH:mm:ss} - {level} - {message}', level='INFO', rotation='1 week', compression='zip')

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Start its Telegram test Bot mirror all message")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
    logger.info(f"{message.from_user.id} Write: {message.text}")


if __name__ == '__main__':
    logger.info("Start Bot")
    executor.start_polling(dp)
