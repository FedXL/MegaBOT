elif message.text == 'Koнсультация':
    await message.answer('Koнсультация', reply_markup=nv.SuperMenu.consMenu)



elif message.text == "Вызов Консультанта":
    await message.answer(f"Если наш FAQ не помог, то {name} ответит на все ваши вопросы.")