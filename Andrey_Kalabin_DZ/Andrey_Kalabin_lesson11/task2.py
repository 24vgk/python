class ErrorZero(ZeroDivisionError):
    def __init__(self, text_error):
        print(text_error)


def division():
    x = int(input('Частное: '))
    y = int(input('Делитель: '))
    try:
        if y == 0:
            raise ErrorZero('Нельзя делить на 0')
        else:
            return x / y
    except ErrorZero('Неизвестная ошибка'):
        pass


if __name__ == "__main__":
    print(division())