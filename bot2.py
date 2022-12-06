import logging
import marka as nv
import random
from texts import make_text_hello, make_text_for_FAQ

from exchange import get_exchange as valut
import aiogram.utils.markdown as md
from aiogram import executor, Bot, Dispatcher, types
from config import NAME
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from utils import ShopValid

name = NAME

try:
    mas = valut()
    eur = (mas[1])
    usd = (mas[0])
except:
    eur = 666
    use = 666

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
bot = Bot(token='5739990172:AAF_gEttCevePt7p2Mi0og-er3XhQRQvcxg')
dp = Dispatcher(bot=bot,
                storage=storage)


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


class Calculator(StatesGroup):
    eurobacs = State()
    getmoney = State()
    result = State()


class Calculator1(StatesGroup):
    eurobacs = State()
    getmoney = State()
    result = State()


@dp.message_handler(commands=['start'], state="*")
async def welcome_message(message: types.Message, state: FSMContext):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await state.finish()
    text = make_text_hello(message.from_user.username)
    await bot.send_message(message.from_user.id, text,
                           reply_markup=nv.SuperMenu.menu,
                           parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['info'], state="*")
async def info_func(message: types.Message, state: FSMContext):
    value = await state.get_state()
    print(value)


@dp.message_handler(Text(equals="Назад"), state="*")
async def back_btn_function(message: types.Message, state: FSMContext):
    value = await state.get_state()
    match value:
        case "TradeInn:login":
            await state.finish()
            await message.answer("Вы вернулись назад в меню заказа",
                                 reply_markup=nv.SuperMenu.invoiceMenu)

        case "TradeInn:pas":
            await state.finish()
            await message.answer("Вы вернулись назад в меню заказа",
                                 reply_markup=nv.SuperMenu.invoiceMenu)

        case "BuyOut:shop":
            await state.finish()
            await message.answer('Вы вернулись назад в меню заказа!',
                                 reply_markup=nv.SuperMenu.invoiceMenu)

        case "BuyOut:login":
            await state.finish()
            await message.answer('Вы вернулись назад в меню заказа!',
                                 reply_markup=nv.SuperMenu.invoiceMenu)

        case "OrderStates:order_kaz_choice":
            await state.finish()
            await message.answer("Меню выбора заказа",
                                 reply_markup=nv.SuperMenu.invoiceMenu)

        case "OrderStates:order_kaz_ch1_shop_name":
            await OrderStates.order_kaz_choice.set()
            await message.answer('Вы вернулись назад! Теперь нам нужно получить либо доступ'
                                 ' к корзине в магазине, '
                                 'либо предоставить прямые ссылки на товары. Выбор за вами:',
                                 reply_markup=nv.SuperMenu.kaz_choice_menu)

        case "OrderStates:ordder_kaz_ch2_href":
            await OrderStates.order_kaz_choice.set()
            await message.answer('Вы вернулись назад! Теперь нам нужно получить либо доступ'
                                 ' к корзине в магазине, '
                                 'либо прямые ссылки на товары. Выбор за вами:',
                                 reply_markup=nv.SuperMenu.kaz_choice_menu)

        case "OrderStates:order_kaz_ch1_loggin":
            await state.finish()
            await OrderStates.order_kaz_choice.set()
            await message.answer('Вы вернулись назад! Теперь нам нужно получить либо доступ'
                                 ' к корзине в магазине, '
                                 'либо прямые ссылки на товары. Выбор за вами:',
                                 reply_markup=nv.SuperMenu.kaz_choice_menu)

        case "OrderStates:order_kaz_ch1_password":
            await state.finish()
            await OrderStates.order_kaz_choice.set()
            await message.answer('Вы вернулись назад! Теперь нам нужно получить либо доступ'
                                 ' к корзине в магазине, '
                                 'либо прямые ссылки на товары. Выбор за вами:',
                                 reply_markup=nv.SuperMenu.kaz_choice_menu)

        case "FAQ:start":
            await state.finish()
            await message.answer('Вы вернулись назад в меню консультаций!',
                                 reply_markup=nv.SuperMenu.consMenu)

        case "Calculator:eurobacs":
            await state.finish()
            await message.answer("Вы вернулись в меню консультаций.", reply_markup=nv.SuperMenu.consMenu)

        case "Calculator:getmoney":
            await state.finish()
            await message.answer("Вы вернулись в меню консультаций.", reply_markup=nv.SuperMenu.consMenu)

        case "Calculator1:eurobacs":
            await state.finish()
            await message.answer("Вы вернулись в меню консультаций.", reply_markup=nv.SuperMenu.consMenu)

        case "Calculator1:getmoney":
            await state.finish()
            await message.answer("Вы вернулись в меню консультаций.", reply_markup=nv.SuperMenu.consMenu)

        case None:
            await message.answer('Вы вернулись в главное меню', reply_markup=nv.SuperMenu.menu)


@dp.message_handler(Text(equals='Заказ Tradeinn'), state=None)
async def tradeinn(message: types.Message):
    await message.answer("Прекрасно! Тогда понадобится логин и пароль от вашего личного кабинета на Tradeinn")
    await TradeInn.login.set()
    await message.answer('Введите логин: ', reply_markup=nv.SuperMenu.cancel)


@dp.message_handler(state=TradeInn.login)
async def tradelogin(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['login'] = message.text
    await message.answer("Ваш логин сохранен!")
    await message.answer("Введите пароль", reply_markup=nv.SuperMenu.cancel)
    await TradeInn.pas.set()


@dp.message_handler(state=TradeInn.pas)
async def tradepass(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['pass'] = message.text
    await message.answer("Ваш заказ отправлен! Скоро с вами свяжется оператор.")
    await message.answer(md.text(
        md.text(md.italic('TradeInn')),
        md.text('Номер заказа:', md.code(random.randint(1000, 9999))),
        md.text('Логин: ', md.bold(data.get('login'))),
        md.text("Пaроль:", md.bold(data.get('pass'))),
        sep='\n'),
        parse_mode=ParseMode.MARKDOWN)
    await state.finish()


@dp.message_handler(Text(equals='Выкуп заказа'), state=None)
async def buyout(message: types.Message):
    await message.answer("Замечательно! В таком случае нам понадобятся: "
                         "Название сайта , пароль и логин от личного кабинета.")
    await message.answer('Введите сайт магазина:', reply_markup=nv.SuperMenu.cancel)
    await BuyOut.shop.set()


@dp.message_handler(state=BuyOut.shop)
async def buyout_get_shop(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['shop'] = message.text
    await message.answer('Сайт успешно сохранён.')
    await message.answer('Введите логин: ', reply_markup=nv.SuperMenu.cancel)
    await BuyOut.login.set()


@dp.message_handler(state=BuyOut.login)
async def buyout_get_login(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['login'] = message.text
    await message.answer('Логин успешно сохранён!')
    await message.answer('Введите пароль:', reply_markup=nv.SuperMenu.cancel)
    await BuyOut.pas.set()


@dp.message_handler(state=BuyOut.pas)
async def buyout_get_login(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['pass'] = message.text
    await message.answer('Ваш заказ отправлен! Скоро с вами свяжется оператор.')
    await message.answer(md.text(
        md.text("ransom"),
        md.text('Заказ номер', md.code(random.randint(1000, 9999))),
        md.text('Магазин: ', md.bold(data.get('shop'))),
        md.text('Логин;', md.bold(data.get('login'))),
        md.text('Пароль: ', md.bold(data.get('pass'))),
        sep='\n'),
        reply_markup=nv.SuperMenu.cancel,
        parse_mode=ParseMode.MARKDOWN)
    await state.finish()


@dp.message_handler(Text(equals='Заказ через Казахстан'), state=None)
async def order_kaz(message: types.Message):
    await OrderStates.order_kaz_choice.set()
    await message.answer('Отлично! Теперь нам нужно получить либо доступ'
                         ' к корзине в магазине, '
                         'либо прямые ссылки на товары. Выбор за вами:',
                         reply_markup=nv.SuperMenu.kaz_choice_menu)


@dp.message_handler(state=OrderStates.order_kaz_choice)
async def order_kaz_choice(message: types.Message, state: FSMContext):
    if message.text == "Предоставлю доступ в личный кабинет":
        async with state.proxy() as data:
            data['kaz_choice'] = 'href'
        await message.answer('Принято! Тогда нам понадобится название'
                             ' магазина, логин и пароль для'
                             ' доступа в личный кабинет и корзине с товарами.')
        await message.answer('Введите название магазина:', reply_markup=nv.SuperMenu.cancel)
        await OrderStates.order_kaz_ch1_shop_name.set()
    elif message.text == "Предоставлю ссылки на товары":
        async with state.proxy() as data:
            data['kaz_choice'] = 'bascet'
        await message.answer(f"Принято! В таком случае нам понадобятся"
                             f" прямые ссылки на каждый из желаемых"
                             f" товаров.\nP.S. ссылка должна быть ПРЯМОЙ, а не из корзины магазина.")
        await message.answer('Введите первую ссылку:', reply_markup=nv.SuperMenu.cancel)
        await OrderStates.ordder_kaz_ch2_href.set()
    else:
        await message.reply('Непонятная команда, используйте кнопки меню для ответа')


@dp.message_handler(state=OrderStates.order_kaz_ch1_shop_name)
async def get_shop_name(message: types.Message, state):
    valid = ShopValid(message.text)
    if not valid:
        await message.reply("что-то пошло не так, не похоже на название магазина попробуйте еще раз:")
    else:
        async with state.proxy() as data:
            data['shop'] = message.text
        await message.answer("Имя магазина успешно сохранено!")
        await message.answer("Введите логин для доступа в личный кабинет:", reply_markup=nv.SuperMenu.cancel)
        await OrderStates.order_kaz_ch1_loggin.set()


@dp.message_handler(state=OrderStates.order_kaz_ch1_loggin)
async def get_shop_name(message: types.Message, state):
    if len(message.text) > 25:
        await message.reply(f"Что-то пошло не так, логин длинный какой то \n"
                            f"на спам похоже. Попробуйте ещё")
    else:
        async with state.proxy() as data:
            data['log'] = message.text
        await message.answer("Логин успешно сохранён!")
        await message.answer("Введите пароль для доступа в личный кабинет:", reply_markup=nv.SuperMenu.cancel)
        await OrderStates.order_kaz_ch1_password.set()


@dp.message_handler(state=OrderStates.order_kaz_ch1_password)
async def get_shop_name(message: types.Message, state):
    if len(message.text) > 35:
        await message.reply(f" Что-то пошло не так, пароль длинный какойто \n"
                            f" на спам похоже. Попробуйте ещё")
    else:
        async with state.proxy() as data:
            data['pass'] = message.text
        await message.answer("Пароль успешно сохранён!")
        await message.answer("Введите пароль для доступа в личный кабинет:", reply_markup=nv.SuperMenu.cancel)
        await bot.send_message(message.chat.id,
                               md.text(
                                   md.text('Номер заказа:', md.code(random.randint(1000, 9999))),
                                   md.text('Магазин: ', md.bold(data['shop'])),
                                   md.text('Логин:   ', md.bold(data['log'])),
                                   md.text('Пароль:  ', md.bold(data['pass'])),
                                   sep='\n'),
                               reply_markup=nv.SuperMenu.cancel,
                               parse_mode=ParseMode.MARKDOWN,
                               )
    await state.finish()
    await message.answer('Ваш заказ отправлен! Ожидайте, оператор с вами свяжется в ближайшее время!',
                         reply_markup=nv.SuperMenu.cancel)


@dp.message_handler(Text(equals='Завершить заказ'),
                    state=OrderStates.ordder_kaz_ch2_href)
async def href(message: types.Message, state: FSMContext):
    text = 'Заказ номер ' + md.code(random.randint(1000, 9999)) + "\n"
    async with state.proxy() as data:
        num = data.get('num')
        for i in range(1, num + 1):
            key = 'href_' + str(i)
            link = data.get(key)
            sstring = str(i) + ". " + link + "\n"
            text += sstring
        await message.answer('Ваш заказ отправлен! Ожидайте, оператор с вами свяжется в ближайшее время!')
        await message.answer(text, parse_mode=ParseMode.MARKDOWN, reply_markup=nv.SuperMenu.cancel)
        await state.finish()


@dp.message_handler(state=OrderStates.ordder_kaz_ch2_href)
async def href(message: types.Message, state: FSMContext):
    vaflalist = (
        'первая',
        'вторая',
        'третья',
        'четвертая',
        'пятая',
        'шестая',
        'седьмая',
        'восьмая',
        'девятая',
        'десятая',
        'одинадцатая',
        'двенадцатая',
        'тринадцатая',
        'четырнадцатая',
        'пятнадцатая')

    async with state.proxy() as data:
        num = data.get('num')
        if num is None:
            data['href_1'] = message.text
            data['num'] = 1
            await message.answer(f'Ваша первая ссылка сохранена')
            await message.answer('Введите ссылку на следующий товар или завершите заказ:',
                                 reply_markup=nv.SuperMenu.kaz_order)
        elif num is not None:
            num = int(num)
            if num <= 14:
                num += 1
                data['num'] = num
                hrefs = 'href_' + str(num)
                data[hrefs] = message.text
                await message.answer(f'Ваша {vaflalist[num - 1]} ссылка сохранена')
                await message.answer(f'Введите ссылку на следующий товар или завершите заказ:',
                                     reply_markup=nv.SuperMenu.kaz_order)
            elif num > 14:
                await message.answer(f'Ваша шестнадцатая ссылка ссылка не сохранена. '
                                     f'Обнаружено превышение здравого смысла. '
                                     f'Лучше передайте контроль над личным кабинетом '
                                     f'Или оформите ещё один заказ.',
                                     reply_markup=nv.SuperMenu.kaz_order)


@dp.message_handler(Text(equals='FAQ'), state=None)
async def hello_faq(message: types.Message):
    await message.answer(md.text(
        md.text("Добро пожаловать в наш ", md.bold('FAQ'), "!"),
        md.text('По каждому из способов доставки мы имеем исчерпывающее руководство.'),
        md.text('Какой способ доставки вас интересует?'),
        sep='\n'),
        reply_markup=nv.SuperMenu.faqMenu,
        parse_mode=ParseMode.MARKDOWN)
    await FAQ.start.set()


@dp.message_handler(state=FAQ.start)
async def generate_faq(message: types.Message):
    if message.text == "Покупка транзитом через Казахстан":
        await message.answer(make_text_for_FAQ(eur, usd, 'var_1_1'),
                             reply_markup=nv.SuperMenu.faqMenu,
                             parse_mode=ParseMode.MARKDOWN)
        await message.answer(md.code(" Тут будет инлайн кнопка сделать заказ"), parse_mode=ParseMode.MARKDOWN)
        await message.answer(make_text_for_FAQ(eur, usd, 'var_1_2'),
                             reply_markup=nv.SuperMenu.faqMenu,
                             parse_mode=ParseMode.MARKDOWN
                             )
    elif message.text == "Покупка на Tradeinn":
        await message.answer(make_text_for_FAQ(eur, usd, 'var_2_1'),
                             parse_mode=ParseMode.MARKDOWN
                             )
        await message.answer(md.code("Тут будет инлайн кнопа сделать заказ"), parse_mode=ParseMode.MARKDOWN)
        await message.answer(
            make_text_for_FAQ(eur, usd, 'var_2_2'),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=nv.SuperMenu.faqMenu
        )
    elif message.text == "Покупка через почтовых посредников":
        await message.answer(make_text_for_FAQ(eur, usd, 'var_3_1'),
                             parse_mode=ParseMode.MARKDOWN,
                             reply_markup=nv.SuperMenu.faqMenu,
                             )
        await message.answer(md.code("Тут будет инлайн кнопка сделать заказ")),
        await message.answer(make_text_for_FAQ(eur, usd, 'var_3_2'),
                             parse_mode=ParseMode.MARKDOWN,
                             reply_markup=nv.SuperMenu.faqMenu)
    else:
        await message.reply("Я такой команды не знаю! Используйте меню для выбора ответа.",
                            reply_markup=nv.SuperMenu.faqMenu)


@dp.message_handler(state=Calculator.eurobacs)
async def calculator_1(message: types.Message, state: FSMContext):
    if message.text in ("Евро", "Доллар"):
        await message.answer(f"Валюта: {message.text}, Теперь введите полную сумму корзины вместе"
                             f" с доставкой в Казахстан:",
                             reply_markup=nv.SuperMenu.cancel)
        await Calculator.getmoney.set()
        async with state.proxy() as data:
            data['eurobaks'] = message.text
    else:
        await message.reply("Непонятная команда, пожалуйста воспользуйтесь кнопками меню.")


@dp.message_handler(state=Calculator.getmoney)
async def getmoney(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        async with state.proxy() as data:
            valuta = data.get('eurobaks')
        if valuta == "Евро":
            valuta = eur
            pref = "Евро"
        elif valuta == "Доллар":
            valuta = usd
            pref = "Доллар"
        else:
            await message.answer(f"Что то пошло сильно не так. Валюта = {valuta}")
            return
    else:
        await message.answer(
            f"Ничего не понимаю. Предыдущее сообщение *{message.text}* не похоже на число. Число должно состоять"
            f"только из цифр, Попробуйте ещё раз.")
        return
    if int(message.text) > 1000:
        total1 = int(message.text) * 1.25 * valuta + 1000 + \
                 (int(message.text) - 1000) * 0.15 * 1.25 * valuta
        total2 = int(message.text) * 1.25 * valuta + 3000 + \
                 (int(message.text) - 1000) * 0.15 * 1.25 * valuta
        text1 = "Cумма к оплате вместе с таможенной пошлиной составит:"
    else:
        total1 = int(message.text) * 1.25 * valuta + 1000
        total2 = int(message.text) * 1.25 * valuta + 3000
        text1 = "Cумма к оплате составит:"
    await message.answer(md.text(
        md.text("Cумма="),
        md.text(" "),
        md.text("Cтоимость корзины с доставкой в Казахстан в валюте"),
        md.text("     x"),
        md.text(f"Биржевой курс валюты"),
        md.text("     x"),
        md.text("1.25 это наша комиссия и затраты на конвертацию"),
        md.text("     +"),
        md.text("Стоимость доставки в РФ (от 1000 руб. до 3000 руб.)"),
        md.text("     +"),
        md.text("Таможенное оформление , если сумма больше 1000 евро"),
        sep="\n"
    ))
    await message.answer(md.text(
        md.text(text1),
        md.text(" "),
        md.text(f"*от {int(total1)} руб.*", f"*до {int(total2)} руб.*", sep=" "),
        md.text(" "),
        md.text("В зависимости от габаритов и веса,"
                " влияет на стоимость доставки в Россию."),
        md.text(" "),
        md.text(f"*Курс валюты на сегодня: 1{pref} = {valuta} рублей.*"),
        md.text(" "),
        sep="\n"),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=nv.SuperMenu.cancel)


@dp.message_handler(state=Calculator1.eurobacs)
async def dollareurocalc2(message: types.Message, state: FSMContext):
    if message.text in ("Евро", "Доллар"):
        await message.answer(f"Валюта: {message.text}, Теперь введите полную сумму корзины вместе"
                             f" с доставкой:",
                             reply_markup=nv.SuperMenu.cancel)
        await Calculator1.getmoney.set()
        async with state.proxy() as data:
            data['eurobaks'] = message.text
    else:
        await message.reply("Непонятная команда, пожалуйста воспользуйтесь кнопками меню.")


@dp.message_handler(state=Calculator1.getmoney)
async def getmoney2(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        async with state.proxy() as data:
            valuta = data.get('eurobaks')
        if valuta == "Евро":
            valuta = eur
            pref = "Евро"
        elif valuta == "Доллар":
            valuta = usd
            pref = "Доллар"
        else:
            await message.answer(f"Что то пошло сильно не так. Валюта = {valuta}")
            return
    else:
        await message.answer(
            f"Ничего не понимаю. Предыдущее сообщение *{message.text}* не похоже на число. Число должно состоять"
            f"только из цифр, Попробуйте ещё раз.")
        return

    if int(message.text) > 1000:
        total = int(message.text) * 1.2 * valuta
        text1 = "Cумма к оплате,без учета таможенной пошлины составит:"
    else:
        total = int(message.text) * 1.2 * valuta
        text1 = "Cумма к оплате составит:"
    await message.answer(md.text(
        md.text("Cумма="),
        md.text(" "),
        md.text("Cтоимость корзины с доставкой."),
        md.text("     x"),
        md.text(f"Биржевой курс валюты"),
        md.text("     x"),
        md.text("1.2 это наша комиссия и затраты на конвертацию"),
        sep="\n"
    ))
    await message.answer(md.text(
        md.text(text1),
        md.text(" "),
        md.text(f"* {int(total)} руб.*"),
        md.text(" "),
        md.text(f"*Курс валюты на сегодня: 1{pref} = {valuta} рублей.*"),
        sep="\n"),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=nv.SuperMenu.cancel)


@dp.message_handler()
async def handler_for_zero_State(message: types.Message):
    if message.text == 'Сделать заказ':
        await message.answer('Отлично!, теперь выбирайте способ заказа.'
                             'Если возникнут трудности всегда можно обратится в раздел Консультации',
                             reply_markup=nv.SuperMenu.invoiceMenu)
        await message.answer(md.code('Тут Будет Сообщение с инлайн кнопкой-ссылкой на FAQ'),
                             reply_markup=nv.SuperMenu.invoiceMenu,
                             parse_mode=ParseMode.MARKDOWN)
    elif message.text == 'Koнсультация':
        await message.answer('Koнсультация', reply_markup=nv.SuperMenu.consMenu)
    elif message.text == "Посчитать примерную стоимость заказа транзитом через Казахстан":
        await Calculator.eurobacs.set()
        await message.answer("Хорошо. Выберите теперь валюту для расчёта:", reply_markup=nv.SuperMenu.EuroBaksMenu)
    elif message.text == "Посчитать примерную стоимость по выкупу заказа":
        await Calculator1.eurobacs.set()
        await message.answer("Хорошо. Выберите теперь валюту для расчёта:", reply_markup=nv.SuperMenu.EuroBaksMenu)
    elif message.text == "Вызов Консультанта":
        await message.answer(f"Если наш FAQ не помог, то {name} ответит на все ваши вопросы.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
