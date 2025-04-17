from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_on_start_main_kb():
    button1 = KeyboardButton(text="/start")
    button2 = KeyboardButton(text="/Settings")
    button3 = KeyboardButton(text="/Info")
    button4 = KeyboardButton(text="/GetNews")
    buttons_row1 = [button1]
    buttons_row2 = [button2]
    buttons_row3 = [button3]
    buttons_row4 = [button4]
    markup = ReplyKeyboardMarkup(keyboard=[buttons_row1, buttons_row2, buttons_row3, buttons_row4], resize_keyboard=True)
    return markup

def get_inline_keyboard_settings():
    btn1 = InlineKeyboardButton(text="Настроить время", callback_data='time')
    btn2 = InlineKeyboardButton(text="Настроить категории", callback_data='categories')
    row = [btn1]
    row2 = [btn2]
    settings_keyboard = InlineKeyboardMarkup(inline_keyboard=[row, row2])
    return settings_keyboard

def cat():
    btn1 = InlineKeyboardButton(text="Наука и техника", callback_data='science')
    btn2 = InlineKeyboardButton(text="Культура", callback_data='culture')
    btn3 = InlineKeyboardButton(text="Экономика", callback_data='economy')
    btn4 = InlineKeyboardButton(text="Мир", callback_data='world')
    btn5 = InlineKeyboardButton(text="Спорт", callback_data='sport')
    cat_keyboard = InlineKeyboardMarkup(inline_keyboard=[[btn1], [btn2], [btn3], [btn4], [btn5]])
    return cat_keyboard