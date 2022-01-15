from random import uniform


def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
           формирует из них единую строковую переменную разделяя значения запятой."""
    print_list = []
    for item in [str(n).split('.') for n in list_in]:
        print_list.append('{} руб {:<02d} коп,'.format(item[0], int(item[1])) if len(item[1]) == 1
                          else '{} руб {} коп,'.format(item[0], item[1]))
    str_out = ' '.join(print_list)
    return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    list_in.sort()
    return list_in


print(id(my_list))
result_2 = sort_prices(my_list)
print(id(result_2))
print(result_2)


def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    list_in.sort()
    list_out = list_in[::-1]
    return list_out


result_3 = sort_price_adv(my_list)
print(result_3)


def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    list_in.sort()
    list_out = list_in[-5:]
    return list_out


result_4 = check_five_max_elements(my_list)
print(result_4)
