import asyncio
from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from create_bot import bot, dp, Settings
from keyboard import get_on_start_main_kb, set
from news import get_news, get_news_keywords
from data_base import db
from callbacks import router
from config import INFO

dp.include_router(router)

@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer(text="Здравствуйте! Настройте бота под себя в Settings",
                         reply_markup=get_on_start_main_kb())
    db.set_user(message.from_user.id)

@dp.message(Command('Settings'))
async def Setting(message: types.Message):
    await message.answer(text="Выберите настройку", reply_markup=set())

@dp.message(Command('Info'))
async def Info(message: types.Message):
    await message.answer(text=INFO)

@dp.message(Command('GetNews'))
async def Get_News(message: types.Message):
    await get_news(message, db.get_cat(message.from_user.id))

@dp.message(Command('Keywords'))
async def keywords_news(message: types.Message):
    await get_news_keywords(message, db.get_keyword(message.from_user.id))

@dp.message(Settings.set_keywords)
async def set_words(message: types.Message, state: FSMContext):
    db.add_keyword(message.from_user.id, message.text.split())
    await state.clear()
    await message.answer(text="Ключевые слова добавлены")

async def main():
    db.db_conect()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


