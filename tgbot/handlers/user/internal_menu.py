from aiogram import Router, F
from aiogram.types import CallbackQuery

from services.wb_service import WildberriesService
from tgbot.keyboards.user import menus

router = Router()


@router.callback_query(menus.CFactory.filter("list_warehouses0" == F.name))
async def list_warehouse(
    callback: CallbackQuery,
    texts: dict,
    wb_service: WildberriesService,
):
    warehouses = await wb_service.get_list_warehouses()
    await callback.message.edit_text(
        text=texts["list_warehouses"],
        reply_markup=menus.create_list_warehouses(list_warehouses=warehouses),
    )


@router.callback_query(menus.CFactory.filter("list_warehouses" == F.name))
async def other_list_warehouses(
    callback: CallbackQuery, texts: dict, wb_service: WildberriesService
):
    warehouses = await wb_service.get_list_warehouses_oth()
    await callback.message.edit_text(
        text=texts["list_warehouses"],
        reply_markup=menus.create_list_warehouses(list_warehouses=warehouses),
    )
