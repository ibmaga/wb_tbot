from aiogram.fsm.state import StatesGroup, State


class UserState(StatesGroup):
    send_token = State()
