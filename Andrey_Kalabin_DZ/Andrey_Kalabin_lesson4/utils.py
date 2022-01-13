from requests import get
from bs4 import BeautifulSoup

def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    soup = BeautifulSoup(response.text, 'lxml')
    name = soup.find_all('charcode')
    value = soup.find_all('value')
    result_dict = {}
    for quote_name, quote_value in zip(name, value):
        x = quote_name.text
        y = quote_value.text
        y = float(y.replace(',', '.'))
        result_dict[x] = y
    if code in result_dict.keys():
        result_value = result_dict[code]
        return result_value