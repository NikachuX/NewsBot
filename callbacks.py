from aiogram import types, F, Router
from create_bot import bot
from keyboard import cat
from data_base import db

router = Router()

@router.callback_query(F.data == 'categories')
async def categories(callback: types.CallbackQuery):
    await callback.message.delete()
    await bot.send_message(callback.from_user.id, text="Выберете категории, которые хотите получать",
                           reply_markup=cat())

@router.callback_query(F.data == 'world')
async def set_categories(callback: types.CallbackQuery):
    await callback.message.delete()
    db.add_cat(callback.from_user.id, 'Мир')
    await bot.send_message(callback.from_user.id, text = "Категория 'мир' добавлена. Выберите еще категории",
                           reply_markup=cat())
