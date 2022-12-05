from pprint import pprint

import requests

def get_exchange():
    try:
        data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    except:
        print("Курс валют не получен")
    usd=data['Valute']['USD']['Value']
    eur=data['Valute']['EUR']['Value']
    print(f'usd {usd},eur {eur}')
    return usd,eur


if __name__ =='__main__':
    get_exchange()
