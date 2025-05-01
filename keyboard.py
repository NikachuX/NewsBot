from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_on_start_main_kb():
    button1 = KeyboardButton(text="/start")
    button2 = KeyboardButton(text="/Settings")
    button3 = KeyboardButton(text="/Info")
    button4 = KeyboardButton(text="/GetNews")
    button5 = KeyboardButton(text="/Keywords")
    markup = ReplyKeyboardMarkup(keyboard=[[button1], [button2], [button3], [button4], [button5]], resize_keyboard=True)
    return markup


def cat():
    btn1 = InlineKeyboardButton(text="Наука и техника", callback_data='science')
    btn2 = InlineKeyboardButton(text="Культура", callback_data='culture')
    btn3 = InlineKeyboardButton(text="Экономика", callback_data='economy')
    btn4 = InlineKeyboardButton(text="Мир", callback_data='world')
    btn5 = InlineKeyboardButton(text="Спорт", callback_data='sport')
    btn6 = InlineKeyboardButton(text="Назад", callback_data='back')
    cat_keyboard = InlineKeyboardMarkup(inline_keyboard=[[btn1], [btn2], [btn3], [btn4], [btn5], [btn6]])
    return cat_keyboard

def set():
    btn1 = InlineKeyboardButton(text = "Добавить категории", callback_data='add')
    btn2 = InlineKeyboardButton(text = "Удалить категории", callback_data='delete')
    btn3 = InlineKeyboardButton(text = "Установить ключевые слова", callback_data='set_keywords')
    btn4 = InlineKeyboardButton(text = "Сбросить ключевые слова", callback_data='reset')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[btn1], [btn2], [btn3], [btn4]])
    return keyboard