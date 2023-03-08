from aiogram import types
from aiogram.utils.markdown import hide_link

import keyboards.main
from config.bot import dp


@dp.message_handler(commands="start")
async def startMessage(message: types.Message) -> None:
    await message.answer(
        text=f"<b>Привет, {message.from_user.first_name}!</b>\n"
        f"Я умный бот Коффи, что желаете выбрать?"
        f"{hide_link(url='https://sberbusiness.live/uploads/media/post_detail/0001/13/thumb_12299_post_detail_tablet.png')}",
        reply_markup=await keyboards.main.keyboard(),
    )
