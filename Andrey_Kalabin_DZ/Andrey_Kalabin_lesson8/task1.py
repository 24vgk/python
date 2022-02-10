import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r'[\w_.+-]+[\w]')
    x = RE_MAIL.findall(email)
    result = {}
    if '.' in x[1]:
        result['username'] = x[0]
        result['domain'] = x[1]
        print(result)
    else:
        raise ValueError(f'wrong email: {email}')


if __name__ == '__main__':
    email_parse('someone@geekbrains.ru')
    email_parse('someone@geekbrainsru')