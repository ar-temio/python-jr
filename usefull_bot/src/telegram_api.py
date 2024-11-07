from src.temperature import get_temperature
from aiogram import Router, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from aiogram.filters import Command
import requests

# Инициализация роутера
router = Router()

# Создание клавиатуры с кнопкой
keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Получить температуру",
                          callback_data="get_temperature")]
])


# Обработчик команды /start
@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Нажмите на кнопку, чтобы узнать текущую температуру.", reply_markup=keyboard)


# Обработчик нажатия на кнопку
@router.callback_query(lambda c: c.data == 'get_temperature')
async def process_callback(callback_query: CallbackQuery):
    temp = get_temperature()
    await callback_query.answer()
    # Отправка нового сообщения с постоянной кнопкой
    await callback_query.message.answer(temp, reply_markup=keyboard)

