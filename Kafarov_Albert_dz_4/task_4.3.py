import requests
from bs4 import BeautifulSoup
from decimal import Decimal
from datetime import datetime


CB_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'


def currency_rates(x):
    x = x.upper()
    full_page = requests.get(CB_URL)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    date = datetime.strptime(soup.find('valcurs').get('date').strip("'"), '%d.%m.%Y').date()
    if x == 'USD' or x == '840':
        convert_USD = Decimal(soup.find('valute', {'id': 'R01235'}).find('value').text.replace(',', '.'))
        return f'На {date} за 1 доллар просят {convert_USD} деревянных'
    elif x == 'EUR' or x == '978':
        convert_EUR = Decimal(soup.find('valute', {'id': 'R01239'}).find('value').text.replace(',', '.'))
        return f'На {date} за 1 евро просят {convert_EUR} деревянных'
    else:
        return


print(currency_rates(input('Введите код валюты: ')))
