import asyncio
from aiogram import types
from aiogram.filters import Command

from create_bot import bot, dp
from keyboard import get_on_start_main_kb, set
from news import get_news
from data_base import db
from callbacks import router


dp.include_router(router)

@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer(text="Здравствуйте! Настройте бота под себя в Settings",
                         reply_markup=get_on_start_main_kb())
    db.set_user(message.from_user.id)

@dp.message(Command('Settings'))
async def Settings(message: types.Message):
    await message.answer(text="Выберите настройку", reply_markup=set())

@dp.message(Command('Info'))
async def Info(message: types.Message):
    await message.answer(text="Информация о боте")

@dp.message(Command('GetNews'))
async def Get_News(message: types.Message):
    await get_news(message, db.get_cat(message.from_user.id))

async def main():
    db.db_conect()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


