









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