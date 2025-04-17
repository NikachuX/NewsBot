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
async def world(callback: types.CallbackQuery):
    await callback.message.delete()
    db.add_cat(callback.from_user.id, 'world', "Мир")
    await bot.send_message(callback.from_user.id, text = "Категория 'Мир' добавлена. Выберите еще категории",
                           reply_markup=cat())

@router.callback_query(F.data == 'sport')
async def sport(callback: types.CallbackQuery):
    await callback.message.delete()
    db.add_cat(callback.from_user.id, 'sport', "Спорт")
    await bot.send_message(callback.from_user.id, text = "Категория 'Спорт' добавлена. Выберите еще категории",
                           reply_markup=cat())

@router.callback_query(F.data == 'culture')
async def culture(callback: types.CallbackQuery):
    await callback.message.delete()
    db.add_cat(callback.from_user.id, 'culture', "Культура")
    await bot.send_message(callback.from_user.id, text = "Категория 'Культура' добавлена. Выберите еще категории",
                           reply_markup=cat())

@router.callback_query(F.data == 'science')
async def science(callback: types.CallbackQuery):
    await callback.message.delete()
    db.add_cat(callback.from_user.id, 'science', "Наука и техника")
    await bot.send_message(callback.from_user.id, text = "Категория 'Наука и техника' добавлена. Выберите еще категории",
                           reply_markup=cat())

@router.callback_query(F.data == 'economy')
async def economy(callback: types.CallbackQuery):
    await callback.message.delete()
    db.add_cat(callback.from_user.id, 'economy', "Экономика")
    await bot.send_message(callback.from_user.id, text = "Категория 'Экономика' добавлена. Выберите еще категории",
                           reply_markup=cat())

@router.callback_query(F.data == 'back')
async def back(callback: types.CallbackQuery):
    await callback.message.delete()
    await bot.send_message(callback.from_user.id, text="Теперь вы можете получать новости по выбранным категориям")