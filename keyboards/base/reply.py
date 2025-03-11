from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


class ReplyKeyboard:
    """Класс для создания reply-клавиатур."""

    def __init__(self, *args: tuple[str, bool], **kwargs: tuple[str, bool]) -> None:
        """
        Инициализация класса.

        :param args: Кортежи с текстом кнопок и флагами запроса контакта или локации.
        :param kwargs: Кортежи с текстом кнопок и флагами запроса контакта или локации.
        """
        self.buttons = args
        self.additional_buttons = kwargs

    def __call__(
        self,
        rows: int = 2,
        resize_keyboard: bool = True,
        one_time_keyboard: bool = False,
    ) -> ReplyKeyboardMarkup:
        """
        Dunder-метод вызова класса как асинхронную функцию для создания reply-клавиатуры.

        :param rows: Количество строк в клавиатуре.
        :param resize_keyboard: Автоматическое изменение размера клавиатуры.
        :param one_time_keyboard: Скрыть клавиатуру после использования.
        :return: Объект класса ReplyKeyboardMarkup.
        """
        builder = ReplyKeyboardBuilder()

        for button in self.buttons:
            text, request_contact_or_location = button
            if request_contact_or_location:
                builder.add(KeyboardButton(text=text, request_contact=True))
            else:
                builder.add(KeyboardButton(text=text))

        for button in self.additional_buttons.values():
            text, request_contact_or_location = button
            if request_contact_or_location:
                builder.add(KeyboardButton(text=text, request_location=True))
            else:
                builder.add(KeyboardButton(text=text))

        builder.adjust(rows)
        return builder.as_markup(
            resize_keyboard=resize_keyboard, one_time_keyboard=one_time_keyboard
        )


if __name__ == "__main__":
    # Пример использования класса ReplyKeyboard для создания клавиатуры главного меню.
    ReplyKeyboard(
        ("Каталог 🛍️", False),
        ("Профиль 👤", False),
        ("Отзывы ⭐️", False),
        ("Поддержка ⚙️", False),
        ("Пригласить друга 🔗", False),
    )(rows=2, resize_keyboard=True, one_time_keyboard=False)
