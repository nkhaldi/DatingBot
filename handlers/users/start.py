from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery
from utils.db_api import db_commands

from keyboards.inline.main_menu_inline import start_keyboard
from aiogram import types
from loader import dp, _


@dp.message_handler(CommandStart())
async def register_user(message: types.Message):
    markup = await start_keyboard()
    try:
        await db_commands.add_user(name=message.from_user.full_name,
                                   telegram_id=message.from_user.id,
                                   username=message.from_user.username)
    except:
        pass
    await message.answer(text=_(f"Приветствую вас, {message.from_user.full_name}!!\n\n"
                                f"<b>❤️️ DATE_BOT</b> - платформа для поиска новых знакомств.\n\n"
                                f"<b>🤝 Сотрудничество: </b>\n"
                                f"Если у вас есть предложение о сотрудничестве, пишите сюда - "
                                f"@borisLobkov\n\n"
                                ),
                         reply_markup=markup)


@dp.callback_query_handler(text="start_menu")
async def start_menu(call: CallbackQuery):
    markup = await start_keyboard()
    await call.message.edit_text(text=_(f"Приветствую вас, {call.from_user.full_name}!!\n\n"
                                        f"<b>❤️️ DATE_BOT</b> - платформа для поиска новых знакомств.\n\n"
                                        f"<b>🤝 Сотрудничество: </b>\n"
                                        f"Если у вас есть предложение о сотрудничестве, пишите сюда - "
                                        f"@borisLobkov\n\n"
                                        ),
                                 reply_markup=markup)


@dp.callback_query_handler(text_contains="lang")
async def change_language(call: CallbackQuery):
    await call.message.edit_reply_markup()
    lang = call.data[-2:]
    await call.message.answer(_("Ваш язык был изменен", locale=lang))
