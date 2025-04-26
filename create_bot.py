from aiogram import Bot, Dispatcher
from config import TOKEN_BOT
from aiogram.fsm.state import StatesGroup, State

bot = Bot(TOKEN_BOT)
dp = Dispatcher()

class Settings(StatesGroup):
    add = State()
    delete = State()