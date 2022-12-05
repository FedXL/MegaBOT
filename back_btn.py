











# @dp.message_handler(Text(equals="Назад"), state=TradeInn.login)
# async def back_btn_order_kaz(message: types.Message, state: FSMContext):
#     await state.finish()
#     await message.answer('Вы вернулись назад в меню заказа!',
#                          reply_markup=nv.SuperMenu.invoiceMenu)

# @dp.message_handler(Text(equals="Назад"), state=TradeInn.pas)
# async def back_btn_order_kaz(message: types.Message, state: FSMContext):
#     await state.finish()
#     await message.answer('Вы вернулись назад в меню заказа!',
#                          reply_markup=nv.SuperMenu.invoiceMenu)

# @dp.message_handler(Text(equals="Назад"), state=BuyOut.shop)
# async def back_btn_order_kaz(message: types.Message, state: FSMContext):
#     await state.finish()
#     await message.answer('Вы вернулись назад в меню заказа!',
#                          reply_markup=nv.SuperMenu.invoiceMenu)

# @dp.message_handler(Text(equals="Назад"), state=BuyOut.login)
# async def back_btn_order_kaz(message: types.Message, state: FSMContext):
#     await state.finish()
#     await message.answer('Вы вернулись назад в меню заказа!',
#                          reply_markup=nv.SuperMenu.invoiceMenu)


# @dp.message_handler(Text(equals="Назад"), state=OrderStates.order_kaz_choice)
# async def back_btn_order_kaz(message: types.Message, state: FSMContext):
#     await state.finish()
#     await message.answer("Меню выбора заказа", reply_markup=nv.SuperMenu.invoiceMenu)


# @dp.message_handler(Text(equals="Назад"),
#                     state=OrderStates.order_kaz_ch1_shop_name)
# async def back_btn_order_kaz(message: types.Message, state: FSMContext):
#     await OrderStates.order_kaz_choice.set()
#     await message.answer('Вы вернулись назад! Теперь нам нужно получить либо доступ'
#                          ' к корзине в магазине, '
#                          'либо прямые ссылки на товары. Выбор за вами:',
#                          reply_markup=nv.SuperMenu.kaz_choice_menu)


# @dp.message_handler(Text(equals="Назад"), state=OrderStates.ordder_kaz_ch2_href)
# async def back_btn_order_kaz(message: types.Message, state: FSMContext):
#     await OrderStates.order_kaz_choice.set()
#     await message.answer('Вы вернулись назад! Теперь нам нужно получить либо доступ'
#                          ' к корзине в магазине, '
#                          'либо прямые ссылки на товары. Выбор за вами:',
#                          reply_markup=nv.SuperMenu.kaz_choice_menu)


# @dp.message_handler(Text(equals="Назад"),
#                     state=OrderStates.order_kaz_ch1_shop_name)
# async def back_btn_order_kaz(message: types.Message, state: FSMContext):
#     await state.finish()
#     await OrderStates.order_kaz_choice.set()
#     await message.answer('Вы вернулись назад! Теперь нам нужно получить либо доступ'
#                          ' к корзине в магазине, '
#                          'либо прямые ссылки на товары. Выбор за вами:',
#                          reply_markup=nv.SuperMenu.kaz_choice_menu)



# @dp.message_handler(Text(equals="Назад"), state=OrderStates.order_kaz_ch1_loggin)
# async def back_btn_order_kaz(message: types.Message, state: FSMContext):
#     await state.finish()
#     await OrderStates.order_kaz_choice.set()
#     await message.answer('Вы вернулись назад! Теперь нам нужно получить либо доступ'
#                          ' к корзине в магазине, '
#                          'либо прямые ссылки на товары. Выбор за вами:',
#                          reply_markup=nv.SuperMenu.kaz_choice_menu)

# @dp.message_handler(Text(equals="Назад"),
#                     state=OrderStates.order_kaz_ch1_password)
# async def back_btn_order_kaz(message: types.Message, state: FSMContext):
#     await state.finish()
#     await OrderStates.order_kaz_choice.set()
#     await message.answer('Вы вернулись назад! Теперь нам нужно получить либо доступ'
#                          ' к корзине в магазине, '
#                          'либо прямые ссылки на товары. Выбор за вами:',
#                          reply_markup=nv.SuperMenu.kaz_choice_menu)

# dp.message_handler(Text(equals="Назад"), state=FAQ.start)
# async def back_btn_order_kaz(message: types.Message, state: FSMContext):
#     await state.finish()
#     await message.answer('Вы вернулись назад в меню консультаций!',
#                          reply_markup=nv.SuperMenu.consMenu)



# @dp.message_handler(Text(equals="Назад"), state=Calculator.eurobacs)
# async def goback(message: types.Message, state: FSMContext):
#     await state.finish()
#     await message.answer("Вы вернулись в меню консультаций.", reply_markup=nv.SuperMenu.consMenu)


# @dp.message_handler(Text(equals="Назад"), state=Calculator.getmoney)
# async def goback(message: types.Message, state: FSMContext):
#     await state.finish()
#     await message.answer("Вы вернулись в меню консультаций.", reply_markup=nv.SuperMenu.consMenu)



# @dp.message_handler(Text(equals="Назад"), state=Calculator1.eurobacs)
# async def goback1(message: types.Message, state: FSMContext):
#     await state.finish()
#     await message.answer("Вы вернулись в меню консультаций.", reply_markup=nv.SuperMenu.consMenu)


@dp.message_handler(Text(equals="Назад"), state=Calculator1.getmoney)
async def goback2(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Вы вернулись в меню консультаций.", reply_markup=nv.SuperMenu.consMenu)