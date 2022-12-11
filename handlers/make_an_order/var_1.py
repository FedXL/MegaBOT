import random
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ParseMode
import utils.markap_menu as nv
from utils.statemachine import OrderStates
from create_bot import bot
import aiogram.utils.markdown as md

from utils.utils_lite import ShopValid

"""______________________Сделать заказ через Казахстан_________________________________"""


async def order_kaz_start_handler(message: types.Message):
    await OrderStates.order_kaz_choice.set()
    await message.answer('Отлично! Теперь нам нужно получить либо доступ'
                         ' к корзине в магазине, '
                         'либо прямые ссылки на товары. Выбор за вами:',
                         reply_markup=nv.SuperMenu.kaz_choice_menu)



async def make_order_kaz_choice(message: types.Message, state: FSMContext):
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



async def get_login(message: types.Message, state):
    if len(message.text) > 25:
        await message.reply(f"Что-то пошло не так, логин длинный какой то \n"
                            f"на спам похоже. Попробуйте ещё")
    else:
        async with state.proxy() as data:
            data['log'] = message.text
        await message.answer("Логин успешно сохранён!")
        await message.answer("Введите пароль для доступа в личный кабинет:", reply_markup=nv.SuperMenu.cancel)
        await OrderStates.order_kaz_ch1_password.set()



async def get_password(message: types.Message, state):
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



async def end_hrefs(message: types.Message, state: FSMContext):
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


async def get_href(message: types.Message, state: FSMContext):
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


def register_handlers_var_1(dp: Dispatcher):
    dp.register_message_handler(order_kaz_start_handler, Text(equals="Заказ через Казахстан"), state=None)
    dp.register_message_handler(make_order_kaz_choice, state=OrderStates.order_kaz_choice)
    dp.register_message_handler(get_shop_name, state=OrderStates.order_kaz_ch1_shop_name)
    dp.register_message_handler(get_login, state=OrderStates.order_kaz_ch1_loggin)
    dp.register_message_handler(get_password, state=OrderStates.order_kaz_ch1_password)
    dp.register_message_handler(end_hrefs, Text(equals='Завершить заказ'), state=OrderStates.ordder_kaz_ch2_href)
    dp.register_message_handler(get_href, state=OrderStates.ordder_kaz_ch2_href)
