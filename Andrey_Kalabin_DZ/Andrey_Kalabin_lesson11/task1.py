class Data:

    def __init__(self, data: str):
        self.data = data

    @classmethod
    def date_number(cls, data: str):
        """
        Извлекает число, месяц, год и преобразовывать их тип к типу «Число»
        :param data: 11-11-1111
        :return: tuple(int, int, int)
        """
        day, mon, year = map(int, data.split('-'))
        if cls.validation(day, mon, year):
            return f'{day}.{mon}.{year}'
        else:
            raise ValueError('Некорректный формат')

    @staticmethod
    def validation(day: int, mon: int, year: int):
        """
        Проверяет дату на соответсвие
        :param day: int
        :param mon: int
        :param year: int
        :return: int, int, int
        """
        if 0 < day < 32 and 0 < mon < 13 and 1900 < year < 2023:
            return day, mon, year
        else:
            raise ValueError('Не верный формат')


if __name__ == '__main__':
    first_data = Data.date_number('12-06-1986')
    print(first_data)
