import aiogram.utils.markdown as md


def make_text_hello(username):
    text_hello = md.text(
        md.text(f"Здравствуйте, *{username}* ! "),
        md.text("Я Бот-Помошник."),
        md.text("Я помогу оформить заказ и знаю ответы "),
        md.text("на большинство ваших вопросов. "),
        md.text("Помогу рассчитать примерную стоимость заказа, а также свяжусь с живым консультантом,"
                " в случае необходимости."),
        sep="\n"
    )
    return text_hello


def make_text_for_FAQ(eur: int, usd: int, value: str):
    """Функция генерирует текст для FAQ весь текст редактировать можно здесь.
    возвращает распарсеный объект текста md.text"""

    value_CAN_BE = ("var_1_1", "var_1_2", "var_2_1", "var_2_2", "var_3_1", "var_3_2")
    assert value in value_CAN_BE, f"Ошибочное value= {value} \n" \
                                  f" доступные значения: \n {value_CAN_BE}"

    match value:
        case "var_1_1":

            text = md.text(
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
                    "*(сумма заказа в валюте вместе с доставкой в казахстан) х (курc) х (1.25) +"
                    " (доставка в россию и таможенная пошлина, если заказ больше 1000 евро)*"),
                md.text(" "),
                md.text(f"Курс сегодня: *{eur}* евро, *{usd}*, доллар"),
                md.text(" "),
                md.text(
                    "Наполняете корзину товарами и даете доступ, мы копируем в свой акаунт. Если корзина небольшая можно"
                    " просто выслать ссылки. Далее вносите предоплату на карту. После отправки заказа магазином,"
                    " мы высылаем вам трек для отслеживания."),
                sep='\n'
            )
        case "var_1_2":
            text = md.text(
                md.text("Забирать в моём сервисе по адресу Москва; ул.Полтавская 35 или вышлю напрямую на ваш адрес."),
                md.text("В этой схеме мы оплачиваем товар, оформляем все необходимые документы для таможни"
                        " и организуем его отправку в Россию при получении. Отправка из Казахстана страхуется"
                        " на полную сумму, срок отправки с момента получения 5 дней."),
                md.text(" "),
                md.text("Риски для покупателя здесь в основном связаны с казахской таможней, но у нас есть"
                        " договор с проверенным таможенным брокером и риски минимизированны."),
                md.text(" "),
                md.text(
                    ("*Доставка СДЕК. Важно!*"),
                    "Если у вас есть малейшие сомнения в целостности послки или она помята,"
                    " вскрывать нужно в пункте СДЭК. Посылка застрахованна на полную сумму."
                    " В накладной СДЭК указан ",
                    md.italic("объемный "),
                    "вес, обычно он заметно больше физического веса."
                ),
                sep="\n"
            )

        case "var_2_1":
            text = md.text(
                md.text("*2 вариант. Bikeinn, Snowinn, Tradeinn. Выкуп товара с прямой доставкой в Россию.*"),
                md.text(" "),
                md.text("Данный вариант только для этого магазина"),
                md.text("Тарифы от 10 000 рублей, комиссия 10%"),
                md.text(" "),
                md.text("* Сумма к оплате Покупателем = (сумма заказа общая с доставкой в руб.) х 1.1 *"),
                md.text(" "),
                md.text("Из плюсов на этом сайте можно купить шимано, гармины и спеш. Если вы не сможете их "
                        "добавить в корзину, я вам помогу. Из минусов на этом сайте достаточно длительные"
                        " сроки отправки и часто нет товаров заявенных как ",
                        md.italic("на складе. "),
                        "Также посылки тут чаще теряются при транспортировке, чем у немцев."
                        ),
                md.text(" "),
                md.text("Если сумма покупки до 300 евро это относительно безрисковая схема, для больших сумм "
                        "или товаров запрещённых к ввозу в Россию я рекомендую пользоваться 1 вариантом. В этой "
                        "схеме я только оплачиваю товар, все остальные риски ваши."),
                md.text(" "),
                md.bold("Возврат"),
                md.text("При отсутствии товара и после возмещения полученного от магазина, я верну эту сумму вам "
                        "без каких либо потерь. Сумма возврата это разница между суммой заказа и счёт-фактурой, "
                        "которая видна после отправки. Возврат идёт в пределах недели с даты отправки заказа. "
                        "При полной отмене заказа я верну всю сумму с комиссией за вычетом 1000р (мин. комиссия). "
                        "Для возврата необходимо написать мне о возврате через неделю после отправки заказа, c указанием "
                        "суммы возврата ( разница между суммой заказа и счёт- фактурой) и даты платежа."),
                md.text(" "),
                md.bold("Что нужно знать при совершении покупок на этом сайте"),
                md.text("1. При заказе обязательно ознакомьтесь со списком товаров запрещённых к вывозу в"
                        " Россию из-за санкций "),
                md.text("2. Если ваш заказ долго не отправляют, пишите в поддержку сайта, соответствующая"
                        " кнопка есть справа от заказа. Если определённого товара нет, лучше его удалить из заказа,"
                        " тогда остальное быстро отправят."),
                md.text(
                    "3. При получении таможенного уведомления по посылке (это бывает очень редко) нужно предоставить "
                    "таможне все требуемые документы, вариант с отказом от посылки и обратной отправкой плохо работает"),
                md.text("4. Защита Покупателя и страховка Route. Все заказы застрахованы страховкой перевозчиков,"
                        " в случае, если вы не получите свой заказ, у вас есь гарантия возврата денег. Есть дополнительный"
                        " вариант страхования Rout, который покрывает риски в случае повреждения кражи или утери, "
                        "а также дополнительно дает вам возможность воспользоваться защитой покупателя Paypal и "
                        "открывать диспут."),
                md.text("5. Оплата на этом сайте при поставке в Россию только с помощью paypal, сколько это продлится "
                        "никто не знает. Если наш paypal заблокируют, то ваши возвраты по причине отсутствия товара, к "
                        "примеру, будут тоже заблокированны."),
                md.text(" "),
                md.text("*Как происходит оплата?*"),
                md.text("Наполняете корзину нужными вам товарами, далее пишите нам и предоставляете доступ к вашему "
                        "аккаунту ( пароль и логин). Я проверяю и пишу сумму к оплате, далее вы перечисляете деньги "
                        "на карту и я оплачиваю ваш заказ, обычно сразу."),
                sep="\n")

        case "var_2_2":
            text = md.text(
                md.text("*Сроки доставки *",
                        " 3-5 недель. ",
                        md.link("Отслеживать здесь", "https://mailingtechnology.com/tracking/")),
                md.text(" "),
                md.text("*Список товаров запрещённых к ввозу в Россию*"),
                md.text("Взято на сайте бандерольки"),
                md.text(
                    "В связи с введёнными санкциями ЕС в данный момент из Европы в Россию нельзя переслать следующее:"),
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
                sep="\n")

        case "var_3_1":
            text = md.text(
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
                sep="\n")
        case "var_3_2":
            text = md.text(
                md.text("*Список товаров запрещённых к ввозу в Россию*"),
                md.text("Взято на сайте бандерольки"),
                md.text(
                    "В связи с введёнными санкциями ЕС в данный момент из Европы в Россию нельзя переслать следующее:"),
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
                sep="\n")

    return text
