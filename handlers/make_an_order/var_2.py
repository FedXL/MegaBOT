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