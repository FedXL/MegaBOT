@dp.message_handler()
async def handler_for_zero_State(message: types.Message):
    if message.text == 'Сделать заказ':
        await message.answer('Отлично!, теперь выбирайте способ заказа.'
                             'Если возникнут трудности всегда можно обратится в раздел Консультации',
                             reply_markup=nv.SuperMenu.invoiceMenu)
        await message.answer(md.code('Тут Будет Сообщение с инлайн кнопкой-ссылкой на FAQ'),
                             reply_markup=nv.SuperMenu.invoiceMenu,
                             parse_mode=ParseMode.MARKDOWN)


