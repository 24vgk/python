from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    x = line.split()
    result = (x[0], x[5][1:], x[6])
    return result


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    while True:
        row = fr.readline()
        if not row:
            break
        list_out.append(get_parse_attrs(row))

pprint(list_out)