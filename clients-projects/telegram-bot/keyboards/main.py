from aiogram import types


async def keyboard() -> None:
    return (
        types.InlineKeyboardMarkup(row_width=2).add(
            types.InlineKeyboardButton(
                text="☕Кофе",
                callback_data="coffee",
            ),
            types.InlineKeyboardButton(
                text="🥐Булочки",
                callback_data="bulochki",
            ),
            types.InlineKeyboardButton(
                text="💳Заказать",
                callback_data="buy",
            ),
            types.InlineKeyboardButton(
                text="🏢Вакансии",
                callback_data="vacancy",
            ),
            types.InlineKeyboardButton(
                text="🕰Часы работы",
                callback_data="time",
            ),
        ),
    )
