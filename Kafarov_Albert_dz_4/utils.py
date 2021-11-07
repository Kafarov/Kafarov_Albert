import requests
from bs4 import BeautifulSoup
from datetime import datetime


def currency_rates(x):
    x = x.upper()
    cb_url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    full_page = requests.get(cb_url)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    date = datetime.strptime(soup.find('valcurs').get('date').strip("'"), '%d.%m.%Y').date()
    elements = soup.find_all('valute')
    value = 0
    for el in elements:
        if el.find('charcode').text == x:
            value = el.find('value').text
            break
    return f'На {date} цена за 1 {x} состовляет {value} рублей'


def currency_dictionary():
    cb_url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    full_page = requests.get(cb_url)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    elements = soup.find_all('valute')
    currency_dict = {}
    for el in elements:
        char_code = el.find('charcode').text
        value = el.find('value').text
        currency_dict[char_code] = value
    return currency_dict
