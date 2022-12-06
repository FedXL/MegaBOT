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
