from datetime import datetime
from requests import get
from bs4 import BeautifulSoup

def currency_rates_adv(code: str):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    soup = BeautifulSoup(response.text, 'lxml')
    name = soup.find_all('charcode')
    value = soup.find_all('value')
    soup1 = BeautifulSoup(response.text, 'html.parser')
    date = soup1.find_all('valcurs')
    list_x = []
    for x in date:
        a = str(x)
        x = a.split('>')
        for i in x[0]:
            if i.isdigit() or i == '.':
                list_x.append(i)
    d = int(''.join(list_x[:2]))
    m = int(''.join(list_x[3:5]))
    ye = int(''.join(list_x[6:]))
    print(ye)
    result_data = datetime(year=ye, month=m, day=d)
    result_dict = {}
    for quote_name, quote_value in zip(name, value):
        x = quote_name.text
        y = quote_value.text
        y = float(y.replace(',', '.'))
        result_dict[x] = y
    if code in result_dict.keys():
        return result_dict[code], result_data

kurs, date_value = currency_rates_adv("USD")
print(kurs, date_value)
print(type(date_value))
empty = bool(not kurs and not date_value)
if not empty and not isinstance(kurs, float):
    raise TypeError("Неверный тип данных у курса")
if not empty and not isinstance(date_value, datetime.date):
    raise TypeError("Неверный тип данных у даты")
print(kurs, date_value)