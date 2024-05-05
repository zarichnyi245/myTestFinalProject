from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_menu_keyboard():
    builder = InlineKeyboardBuilder()

    builder.button(text="Перелік фільмів", callback_data=f"films")
    builder.button(text="Додати новий фільм", callback_data=f"filmcreate")

    return builder.as_markup()

