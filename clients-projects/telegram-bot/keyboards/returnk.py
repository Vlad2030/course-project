from aiogram import types


async def keyboard() -> None:
    return types.InlineKeyboardMarkup(row_width=2).add(
        types.InlineKeyboardButton(text="↩Назад", callback_data="return")
    )
