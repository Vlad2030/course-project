from aiogram import executor
from config.bot import dp

if "__main__" == __name__:
    executor.start_polling(dp, skip_updates=True)
