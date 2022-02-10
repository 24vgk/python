class Digit(ValueError):
    def __init__(self, text):
        pass


res = []
while True:
    number = input('Вводите числа для создания списка-при вводе слова "stop" ввод закончится: ')
    try:
        if number == 'stop':
            break
        elif not number.isdigit():
            raise Digit('Вы ввели НЕ число')
        else:
            res.append(int(number))
    except (ValueError, Digit) as er:
        print(er)
print(res)