from aiogram import types
from aiogram.utils.markdown import hide_link

import keyboards.main
import keyboards.returnk
from config.bot import dp, bot


@dp.callback_query_handler(text="coffee")
async def callbackCoffee(callback_query: types.CallbackQuery) -> None:
    pass


@dp.callback_query_handler(text="bulochki")
async def callbackBulochki(callback_query: types.CallbackQuery) -> None:
    pass


@dp.callback_query_handler(text="buy")
async def callbackBuy(callback_query: types.CallbackQuery) -> None:
    pass


@dp.callback_query_handler(text="vacancy")
async def callbackVacancy(callback_query: types.CallbackQuery) -> None:
    pass


@dp.callback_query_handler(text="time")
async def callbackTime(callback_query: types.CallbackQuery) -> None:
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text="Мы работаем для вас с 9:00 до 22:00\n\n"
        "Наш адрес:\nСтолярный переулок, дом 3, корпус 14. Вход с крыльца",
        reply_markup=await keyboards.returnk.keyboard(),
    )


@dp.callback_query_handler(text="return")
async def callbackReturn(callback_query: types.CallbackQuery) -> None:
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=f"<b>Привет, {callback_query.from_user.first_name}!</b>\n"
        f"Я умный бот Коффи, что желаете выбрать?"
        f"{hide_link('https://sberbusiness.live/uploads/media/post_detail/0001/13/thumb_12299_post_detail_tablet.png')}",
        reply_markup=await keyboards.main.keyboard(),
    )
