from src.telegram_api import router
from src.commands import set_commands
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
import asyncio
import logging
import os


# Основная функция запуска бота
async def main():
    # Инициализация логирования
    logging.basicConfig(level=logging.INFO)

    # Токен бота
    API_TOKEN = os.getenv("TG_TOKEN")

    # Создание экземпляра бота и диспетчера
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()

    # Регистрация роутера
    dp.include_router(router)

    await set_commands(bot)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

# Запуск бота
if __name__ == "__main__":
    asyncio.run(main())
