from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.markdown import hide_link


api_token = '5857994153:AAEfm0gwuI5Zp3cMR1AUKDT4y2IgqjIP_Fc'

bot = Bot(token=api_token,
    parse_mode=types.ParseMode.HTML
)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


def mainKeyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton(
            text="☕Кофе",
            callback_data="coffee"
        ),
        types.InlineKeyboardButton(
            text="🥐Булочки",
            callback_data="bulochki"
        ),
        types.InlineKeyboardButton(
            text="💳Заказать",
            callback_data="buy"
        ),
        types.InlineKeyboardButton(
            text="🏢Вакансии",
            callback_data="vacancy"
        ),
        types.InlineKeyboardButton(
            text="🕰Часы работы",
            callback_data="time"
        )
    )
    return keyboard



def returnKeyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton(
            text="↩Назад",
            callback_data="return"
        )
    )
    return keyboard


@dp.message_handler(commands='start')
async def startMessage(message: types.Message) -> None:
    await message.answer(
        text=f"<b>Привет, {message.from_user.first_name}!</b>\n"
            f"Я умный бот Коффи, что желаете выбрать?"
            f"{hide_link('https://sberbusiness.live/uploads/media/post_detail/0001/13/thumb_12299_post_detail_tablet.png')}",
        reply_markup=mainKeyboard(),
    )


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
        text='Мы работаем для вас с 9:00 до 22:00\n\n'
        'Наш адрес:\nСтолярный переулок, дом 3, корпус 14. Вход с крыльца',
        reply_markup=returnKeyboard(),
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
        reply_markup=mainKeyboard(),
    )

if "__main__" == __name__:
    executor.start_polling(dp, skip_updates=True)