from aiogram import types, F, Router
from aiogram.fsm.context import FSMContext

from create_bot import bot, Settings
from keyboard import cat
from data_base import db

router = Router()

@router.callback_query(F.data == 'world')
async def world(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    curr_state = await state.get_state()
    word = ""
    if curr_state == Settings.delete:
        db.del_cat(callback.from_user.id, 'world')
        word = "удалена"
    if curr_state == Settings.add:
        db.add_cat(callback.from_user.id, 'world', 'Мир')
        word = "добавлена"
    await bot.send_message(callback.from_user.id, text = f"Категория 'Мир' {word}. Выберите еще категории",
                           reply_markup=cat())

@router.callback_query(F.data == 'sport')
async def sport(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    curr_state = await state.get_state()
    word = ""
    if curr_state == Settings.delete:
        db.del_cat(callback.from_user.id, 'sport')
        word = "удалена"
    if curr_state == Settings.add:
        db.add_cat(callback.from_user.id, 'sport', "Спорт")
        word = "добавлена"
    await bot.send_message(callback.from_user.id, text = f"Категория 'Спорт' {word}. Выберите еще категории",
                           reply_markup=cat())

@router.callback_query(F.data == 'culture')
async def culture(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    curr_state = await state.get_state()
    word = ""
    if curr_state == Settings.delete:
        db.del_cat(callback.from_user.id, 'culture')
        word = "удалена"
    if curr_state == Settings.add:
        db.add_cat(callback.from_user.id, 'culture', "Культура")
        word = "добавлена"
    await bot.send_message(callback.from_user.id, text = f"Категория 'Культура' {word}. Выберите еще категории",
                           reply_markup=cat())

@router.callback_query(F.data == 'science')
async def science(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    curr_state = await state.get_state()
    word = ""
    if curr_state == Settings.delete:
        db.del_cat(callback.from_user.id, 'science')
        word = "удалена"
    if curr_state == Settings.add:
        db.add_cat(callback.from_user.id, 'science', "Наука и техника")
        word = "добавлена"
    await bot.send_message(callback.from_user.id, text = f"Категория 'Наука и техника' {word}. Выберите еще категории",
                           reply_markup=cat())

@router.callback_query(F.data == 'economy')
async def economy(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    curr_state = await state.get_state()
    word = ""
    if curr_state == Settings.delete:
        db.del_cat(callback.from_user.id, 'economy')
        word = "удалена"
    if curr_state == Settings.add:
        db.add_cat(callback.from_user.id, 'economy', "Экономика")
        word = "добавлена"
    await bot.send_message(callback.from_user.id, text = f"Категория 'Экономика' {word}. Выберите еще категории",
                           reply_markup=cat())

@router.callback_query(F.data == 'back')
async def back(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await state.clear()
    await bot.send_message(callback.from_user.id, text="Теперь вы можете получать новости по выбранным категориям")

@router.callback_query(F.data == 'add')
async def add(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await state.set_state(Settings.add)
    await bot.send_message(callback.from_user.id, text="Выберете категории, которые хотите получать",
                           reply_markup=cat())

@router.callback_query(F.data == 'delete')
async def delete(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await state.set_state(Settings.delete)
    await bot.send_message(callback.from_user.id, text="Выберете категории, которые хотите удалить",
                           reply_markup=cat())

@router.callback_query(F.data == 'set_keywords')
async def set_key(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await state.set_state(Settings.set_keywords)
    await bot.send_message(callback.from_user.id, text="Введите ключевые слова по которым хотите получать новости через пробел")

@router.callback_query(F.data == 'reset')
async def reset(callback: types.CallbackQuery):
    await callback.message.delete()
    db.reset_keywords(callback.from_user.id)
    await bot.send_message(callback.from_user.id, text="Ключевые слова сброшены")