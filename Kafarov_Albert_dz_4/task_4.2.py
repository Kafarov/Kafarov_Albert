import requests
from bs4 import BeautifulSoup
from decimal import Decimal


CB_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'


def currency_rates(x):
    x = x.upper()
    full_page = requests.get(CB_URL)
    soup = BeautifulSoup(full_page.content, 'lxml')
    if x == 'USD' or x == '840':
        convert_USD = Decimal(soup.find('valute', {'id': 'R01235'}).find('value').text.replace(',', '.'))
        return convert_USD
    elif x == 'EUR' or x == '978':
        convert_EUR = Decimal(soup.find('valute', {'id': 'R01239'}).find('value').text.replace(',', '.'))
        return convert_EUR
    else:
        return


print(currency_rates(input('Введите код валюты: ')))
