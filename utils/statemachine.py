from aiogram.dispatcher.filters.state import StatesGroup, State


class OrderStates(StatesGroup):
    order_kaz_choice = State()
    order_kaz_ch1_shop_name = State()
    order_kaz_ch1_loggin = State()
    order_kaz_ch1_password = State()
    ordder_kaz_ch2_href = State()
    menu = State()
    advice = State()


class TradeInn(StatesGroup):
    login = State()
    pas = State()


class BuyOut(StatesGroup):
    shop = State()
    login = State()
    pas = State()


class FAQ(StatesGroup):
    start = State()


class Calculator_1(StatesGroup):
    eurobacs = State()
    getmoney = State()
    result = State()


class Calculator_2(StatesGroup):
    eurobacs = State()
    getmoney = State()
    result = State()