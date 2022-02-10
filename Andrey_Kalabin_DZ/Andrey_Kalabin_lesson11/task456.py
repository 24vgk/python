import pprint

class OfficeEquipment:

    def __init__(self, name, sn, dimensions):
        self.group = self.__class__.__name__
        self.name = name
        self.sn = sn
        if type(dimensions) == str and 'x' in dimensions:
            self.dimensions = dimensions
        else:
            raise TypeError('Не верный формат ввода параметра устройства dimensions! Необходимый формат 111X111')

    def name_group(self):
        return f'{self.group}'

    def __repr__(self):
        return f'(Наименование: {self.name}, серийный номер: {self.sn}, габариты: {self.dimensions})'



class Printer(OfficeEquipment):

    def __init__(self, name: str, sn: str, dimensions: str, collor: str):
        super().__init__(name, sn, dimensions)
        self.collor = collor

    def action(self):
        return f'{self.__class__.__name__} - Распечатывает'


class Scaner(OfficeEquipment):

    def __init__(self, name: str, sn: str, dimensions: str, permission: int):
        super().__init__(name, sn, dimensions)
        self.permission = permission

    def action(self):
        return f'{self.__class__.__name__} - Сканирует'


class Xerox(OfficeEquipment):

    def __init__(self, name, sn, dimensions, speed):
        super().__init__(name, sn, dimensions)
        self.speed = speed

    def action(self):
        return f'{self.__class__.__name__} - Копирует'


class ShedWithJunk:

    def __init__(self, name):
        self._dict = {}
        self.lst = []
        self.name = name

    def load_equip(self, equipment):
        if isinstance(equipment, OfficeEquipment):
            self._dict.setdefault(equipment.name_group(), []).append(equipment)
        else:
            raise ValueError('ERROR')

    # def disposal(self, name, sn):
    #     if self._dict[name]:
    #         for i in self._dict[name]:
    #             x = str(i)
    #             a = x.index(self._dict[name])
    #             print(a)
    #             if x.find(sn):
    #                 self._dict.setdefault(name).pop(a)
    #             else:
    #                 continue



if __name__ == '__main__':
    try:
        junk = ShedWithJunk('1')

        scaner = Scaner('HP', '111TR', '50x50', 1500)
        junk.load_equip(scaner)
        print(scaner.action())

        scaner = Scaner('Xerox', '222', '100x100', '1200')
        junk.load_equip(scaner)

        scaner = Scaner('HP', '333', '150x150', 3000)
        junk.load_equip(scaner)

        xerox = Xerox('Xerox', '444', '150x150', 'Black')
        junk.load_equip(xerox)
        print(xerox.action())

        printer = Printer('Sony', '333', '150x150', 'Black')
        junk.load_equip(printer)
        print(printer.action())

        print(junk._dict)
        junk.disposal('Scaner', '222')
        print()
        print(junk._dict)
    except TypeError as er:
        print(er)
