import logging
import marka as nv
import random
from texts import text_1, make_text_hello

from exchange import get_exchange as valut
import aiogram.utils.markdown as md
from aiogram import executor, Bot, Dispatcher, types
from config import TOKEN_API, NAME
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



idd = 716336613


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


@dp.message_handler(Text(equals='Заказ Tradeinn'), state=None)
async def tradeinn(message: types.Message):
    await message.answer("Прекрасно! Тогда понадобится логин и пароль от вашего личного кабинета на Tradeinn")
    await TradeInn.login.set()
    await message.answer('Введите логин: ', reply_markup=nv.SuperMenu.cancel)


@dp.message_handler(Text(equals="Назад"), state=TradeInn.login)
async def back_btn_order_kaz(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Вы вернулись назад в меню заказа!',
                         reply_markup=nv.SuperMenu.invoiceMenu)


@dp.message_handler(Text(equals="Назад"), state=TradeInn.pas)
async def back_btn_order_kaz(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Вы вернулись назад в меню заказа!',
                         reply_markup=nv.SuperMenu.invoiceMenu)


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


@dp.message_handler(Text(equals="Назад"), state=BuyOut.shop)
async def back_btn_order_kaz(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Вы вернулись назад в меню заказа!',
                         reply_markup=nv.SuperMenu.invoiceMenu)


@dp.message_handler(Text(equals="Назад"), state=BuyOut.login)
async def back_btn_order_kaz(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Вы вернулись назад в меню заказа!',
                         reply_markup=nv.SuperMenu.invoiceMenu)


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


@dp.message_handler(Text(equals="Назад"), state=OrderStates.order_kaz_choice)
async def back_btn_order_kaz(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Меню выбора заказа", reply_markup=nv.SuperMenu.invoiceMenu)


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


@dp.message_handler(Text(equals="Назад"),
                    state=OrderStates.order_kaz_ch1_shop_name)
async def back_btn_order_kaz(message: types.Message, state: FSMContext):
    await OrderStates.order_kaz_choice.set()
    await message.answer('Вы вернулись назад! Теперь нам нужно получить либо доступ'
                         ' к корзине в магазине, '
                         'либо прямые ссылки на товары. Выбор за вами:',
                         reply_markup=nv.SuperMenu.kaz_choice_menu)


@dp.message_handler(Text(equals="Назад"), state=OrderStates.ordder_kaz_ch2_href)
async def back_btn_order_kaz(message: types.Message, state: FSMContext):
    await OrderStates.order_kaz_choice.set()
    await message.answer('Вы вернулись назад! Теперь нам нужно получить либо доступ'
                         ' к корзине в магазине, '
                         'либо прямые ссылки на товары. Выбор за вами:',
                         reply_markup=nv.SuperMenu.kaz_choice_menu)


@dp.message_handler(Text(equals="Назад"),
                    state=OrderStates.order_kaz_ch1_shop_name)
async def back_btn_order_kaz(message: types.Message, state: FSMContext):
    await state.finish()
    await OrderStates.order_kaz_choice.set()
    await message.answer('Вы вернулись назад! Теперь нам нужно получить либо доступ'
                         ' к корзине в магазине, '
                         'либо прямые ссылки на товары. Выбор за вами:',
                         reply_markup=nv.SuperMenu.kaz_choice_menu)


@dp.message_handler(Text(equals="Назад"), state=OrderStates.ordder_kaz_ch2_href)
async def back_btn_order_kaz(message: types.Message, state: FSMContext):
    await state.finish()
    await OrderStates.order_kaz_choice.set()
    await message.answer('Вы вернулись назад! Теперь нам нужно получить либо доступ'
                         ' к корзине в магазине, '
                         'либо прямые ссылки на товары. Выбор за вами:',
                         reply_markup=nv.SuperMenu.kaz_choice_menu)


@dp.message_handler(Text(equals="Назад"), state=OrderStates.order_kaz_ch1_loggin)
async def back_btn_order_kaz(message: types.Message, state: FSMContext):
    await state.finish()
    await OrderStates.order_kaz_choice.set()
    await message.answer('Вы вернулись назад! Теперь нам нужно получить либо доступ'
                         ' к корзине в магазине, '
                         'либо прямые ссылки на товары. Выбор за вами:',
                         reply_markup=nv.SuperMenu.kaz_choice_menu)


@dp.message_handler(Text(equals="Назад"),
                    state=OrderStates.order_kaz_ch1_password)
async def back_btn_order_kaz(message: types.Message, state: FSMContext):
    await state.finish()
    await OrderStates.order_kaz_choice.set()
    await message.answer('Вы вернулись назад! Теперь нам нужно получить либо доступ'
                         ' к корзине в магазине, '
                         'либо прямые ссылки на товары. Выбор за вами:',
                         reply_markup=nv.SuperMenu.kaz_choice_menu)


@dp.message_handler(Text(equals="Назад"), state=FAQ.start)
async def back_btn_order_kaz(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Вы вернулись назад в меню консультаций!',
                         reply_markup=nv.SuperMenu.consMenu)


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
        hrefs_num = ['href_' + str(i) for i in range(1, num + 1)]
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
                href = 'href_' + str(num)
                data[href] = message.text
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
async def fAq(message: types.Message):
    await message.answer(md.text(
        md.text("Добро пожаловать в наш ", md.bold('FAQ'), "!"),
        md.text('По каждому из способов доставки мы имеем исчерпывающее руководство.'),
        md.text('Какой способ доставки вас интересует?'),
        sep='\n'),
        reply_markup=nv.SuperMenu.faqMenu,
        parse_mode=ParseMode.MARKDOWN)
    await FAQ.start.set()


@dp.message_handler(state=FAQ.start)
async def Faq(message: types.Message):
    if message.text == "Покупка транзитом через Казахстан":
        await message.answer(md.text(
            md.text("*1й Вариант. Покупка транзитом через Казахстан.*"),
            md.text(" "),
            md.text("В Казахстан шлют все основные велосипедные магазины: bike-discount.de, "
                    "bike-components.de, chainreactioncycles.com, wiggle.com. Эта схема без"
                    " европейского НДС. "),
            md.text("r2-bike.com b bike24.com не шлют в Казахстан, для них подходит 3тий вариант."),
            md.text("По зимнему снаряжению доставка в Казахстан есть в snowinn.com, skicenter.it, snowcountry.eu."),
            md.text(" "),
            md.text("Перед заказом убедитесь , что магазин шлёт в Казахстан вообще и ваши товары в частности, для "
                    "этого достаточно сменить страну доставки на Казахстан."),
            md.text(" "),
            md.text(md.bold("Заказ от 500 евро"),
                    ", групповые заказы мы не собираем, но вы можете самостоятельно кооперироваться."
                    " Доставка в Россию с Казахстана Сдеком 1-3 тыс.руб со страховкой, если "
                    "негабарит типа колес или лыж то 3-5 тыс.руб, велосипед в сборе около 7 тыс.руб. "
                    "Если посылка идет экспресс доставками, то есть дополнительный сбор для таможенного "
                    "оформления 3500 теньге (500 рублей). Таможенный лимит для беспошлинного ввоза сейчас "
                    "1000 евро."),
            md.text(" "),
            md.text("*Сумма к оплате Покупателем=*"),
            md.text(
                "*(сумма заказа в валюте вместе с доставкой в казахстан) х (курc) х (1.25) + (доставка в россию и таможенная пошлина, если заказ больше 1000 евро)*"),
            md.text(" "),
            md.text(f"Курс сегодня: {eur} евро, {usd}, доллар"),
            md.text(" "),
            md.text(
                "Наполняете корзину товарами и даете доступ, мы копируем в свой акаунт. Если корзина небольшая можно просто"
                " выслать ссылки. Далее вносите предоплату на карту. После отправки заказа магазином, мы высылаем вам трек для"
                " отслеживания."),
            sep='\n'),
            reply_markup=nv.SuperMenu.faqMenu,
            parse_mode=ParseMode.MARKDOWN)
        await message.answer(md.code(" Тут будет инлайн кнопка сделать заказ"), parse_mode=ParseMode.MARKDOWN)
        await message.answer(md.text(
            md.text("Забирать в моём сервисе по адресу Москва; ул.Полтавская 35 или вышлю напрямую на ваш адрес."),
            md.text(
                "В этой схеме мы оплачиваем товар, оформляем все необходимые документы для таможни и организуем его отправку в Россию при получении."
                "Отправка из Казахстана страхуется на полную сумму, срок отправки с момента получения 5 дней."),
            md.text(" "),
            md.text(
                "Риски для покупателя здесь в основном связаны с казахской таможней, но у нас есть договор с проверенным таможенным брокером и риски минимизированны."),
            md.text(" "),
            md.text(("*Доставка СДЕК. Важно!*"),
                    "Если у вас есть малейшие сомнения в целостности послки или она помята, вскрывать нужно в пункте СДЭК."
                    "Посылка застрахованна на полную сумму. В накладной СДЭК указан ", md.italic("объемный "),
                    "вес, обычно он "
                    "заметно больше физического веса."),
            sep="\n"
        ),
            reply_markup=nv.SuperMenu.faqMenu,
            parse_mode=ParseMode.MARKDOWN
        )
    elif message.text == "Покупка на Tradeinn":
        await message.answer(text_1,
            parse_mode=ParseMode.MARKDOWN
        )
        await message.answer(md.code("Тут будет инлайн кнопа сделать заказ"), parse_mode=ParseMode.MARKDOWN)
        await message.answer(md.text(
            md.text("*Сроки доставки *", "3-5 недель. ",
                    md.link("Отслеживать здесь", "https://mailingtechnology.com/tracking/")),
            md.text(" "),
            md.text("*Список товаров запрещённых к ввозу в Россию*"),
            md.text("Взято на сайте бандерольки"),
            md.text("В связи с введёнными санкциями ЕС в данный момент из Европы в Россию нельзя переслать следующее:"),
            md.text(
                "Товары стоимостью выше 300 евро, если это косметика, одежда, обувь, аксессуары, спортивные товары, "
                "ювелирные изделия и другие повседневные товары;"),
            md.text("Бытовая техника свыше 750 евро за единиу товара;"),
            md.text("Фото и видеокамеры, а также фотовспышки соимостью выше 1000 евро"),
            md.text("Музыкальные инструменты стоимостью выше 1500 евро."),
            md.text(" "),
            md.link("Список бандерольки", "https://qwintry.com/ru/forbidden-goods"),
            md.text(" "),
            md.link("Официальный список", "https://www.alta.ru/tnved/forbidden_codes"),
            sep="\n"),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=nv.SuperMenu.faqMenu
        )
    elif message.text == "Покупка через почтовых посредников":
        await message.answer(md.text(
            md.text("*3 вариант. Выкуп товара. Поставка через почтового посредника.*"),
            md.text("По этой схеме можно купить во всех стандартных интернет магазинах."
                    " Заказ от 200 евро"),
            md.text("Вы заказываете через посредника типа",
                    md.link("бандерольки", "https://qwintry.com/ru/kz"),
                    ",",
                    md.link("shipito", "https://www.shipito.com"),
                    ",",
                    md.link("alfaparcel", "https://alfaparcel.com/"),
                    "и прочие, если нет аккаунта то регистрируетесь. В интернет-магазине в качестве почтового "
                    "адреса ставите местный адрес, который выдает посредник.",
                    sep=" "),
            md.text("Кроме того есть велосипедные магазины ",
                    md.link("starbike", "https://www.starbike.ru/"),
                    ",",
                    md.link("bikehit", "https://www.bikehit.de/de/"),
                    "поставляющие напрямую в Россию, правда товары до 300 евро только, в них выкупаю по тем же"
                    " расценкам.",
                    sep=" "),
            md.text(" "),
            md.text("Если вы покупаете в европе то минус этой схемы в том, что вы платите европейский ват(ндс),"
                    "при покупке в штатах ндс нет."),
            md.text(" "),
            md.text("В этой схеме мы только оплачиваем товар и взаимодействуем с вами на этапе покупки в "
                    "выбраном интернет-магазине, все остальные операции осуществляет бандеролька или другой"
                    " почтовый посредник. Схема рабочая и сейчас самая распространенная схема покупки в Россию. "
                    "Скорость прохождения заказов разная, неделю где-то посылка ждёт переупаковки и бывают "
                    "затыки на европейской таможне. В среднем с европы за месяц приходит, со штатов приблизительно "
                    "также. Стоимость доставки через бандерольку немного выше, чем у магазинов и стандартных "
                    "почтовых служб. Например доставка 5кг посылки со штатов стоит около 100 долларов."),
            md.text(" "),
            md.text("Перед заказом убедитесь , что вы не покупаете товары попадающие под санкции (см. ниже "
                    "или на сайте бандерольки), если есть малейшие сомнения то спрашивайте саппорт почтового "
                    "посредника."),
            md.text(" "),
            md.text("*Сумма к оплате Покупателем = (сумма заказа общая с доставкой до местного адреса в валюте) х "
                    "1.2 х (биржевой курс) *"),
            md.text(" "),
            md.text(f"Курс сегодня: {eur} евро, {usd}, доллар"),
            md.text(" "),
            md.text("Да конечно вы можете всё сделать самостоятельно через бандерольку без нас. Но выкуп товара "
                    "у нас дешевле. Кроме того многие вопросы связанные с заказми (замена товара, возвраты и т.д.) "
                    "мы решаем более оперативно."),
            sep="\n"),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=nv.SuperMenu.faqMenu,

        )
        await message.answer(md.code("Тут будет инлайн кнопка сделать заказ")),
        await message.answer(md.text(
            md.text("*Список товаров запрещённых к ввозу в Россию*"),
            md.text("Взято на сайте бандерольки"),
            md.text("В связи с введёнными санкциями ЕС в данный момент из Европы в Россию нельзя переслать следующее:"),
            md.text(
                "Товары стоимостью выше 300 евро, если это косметика, одежда, обувь, аксессуары, спортивные товары, "
                "ювелирные изделия и другие повседневные товары;"),
            md.text("Бытовая техника свыше 750 евро за единиу товара;"),
            md.text("Фото и видеокамеры, а также фотовспышки соимостью выше 1000 евро"),
            md.text("Музыкальные инструменты стоимостью выше 1500 евро."),
            md.text(" "),
            md.link("Список бандерольки", "https://qwintry.com/ru/forbidden-goods"),
            md.text(" "),
            md.link("Официальный список", "https://www.alta.ru/tnved/forbidden_codes"),
            sep="\n"),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=nv.SuperMenu.faqMenu)
    else:
        await message.reply("Я такой команды не знаю! Используйте меню для выбора ответа.",
                            reply_markup=nv.SuperMenu.faqMenu)


@dp.message_handler(Text(equals="Назад"), state=Calculator.eurobacs)
async def goback(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Вы вернулись в меню консультаций.", reply_markup=nv.SuperMenu.consMenu)


@dp.message_handler(Text(equals="Назад"), state=Calculator.getmoney)
async def goback(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Вы вернулись в меню консультаций.", reply_markup=nv.SuperMenu.consMenu)


@dp.message_handler(state=Calculator.eurobacs)
async def dollareurocalc(message: types.Message, state: FSMContext):
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


@dp.message_handler(Text(equals="Назад"), state=Calculator1.eurobacs)
async def goback1(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Вы вернулись в меню консультаций.", reply_markup=nv.SuperMenu.consMenu)


@dp.message_handler(Text(equals="Назад"), state=Calculator1.getmoney)
async def goback2(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Вы вернулись в меню консультаций.", reply_markup=nv.SuperMenu.consMenu)


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
async def masmes(message: types.Message):
    if message.text == 'Сделать заказ':
        await message.answer('Отлично!, теперь выбирайте способ заказа.'
                             'Если возникнут трудности всегда можно обратится в раздел Консультации',
                             reply_markup=nv.SuperMenu.invoiceMenu)
        await message.answer(md.code('Тут Будет Сообщение с инлайн кнопкой-ссылкой на FAQ'),
                             reply_markup=nv.SuperMenu.invoiceMenu,
                             parse_mode=ParseMode.MARKDOWN)
    elif message.text == 'Koнсультация':
        await message.answer('Koнсультация', reply_markup=nv.SuperMenu.consMenu)
    elif message.text == 'Назад':
        await message.answer('Вы вернулись в главное меню', reply_markup=nv.SuperMenu.menu)
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
