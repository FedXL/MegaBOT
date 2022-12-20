from collections import namedtuple
import requests

rate = namedtuple("Rate", "eur usd date")


def get_exchange():
    try:
        data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    except:
        print("Курс валют не получен")
    usd = data['Valute']['USD']['Value']
    eur = data['Valute']['EUR']['Value']
    print(f'usd {usd},eur {eur}')
    date = (data['Timestamp'].split('T'))
    return rate(eur=eur, usd=usd, date=date)


if __name__ == '__main__':
    get_exchange()
