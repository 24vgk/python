import os


def rounding(num):
    """
    функция окрукгления кратно 10
    :param num: int
    :return: int
    """
    num_x = 10**(len(str(num)))
    return num_x


def dir_file():
    """
    Перебирает все папки и файлы относительно адреса данного файла. Выдает словарь ключи - Имена файлов
    значения - объем ключей
    :return:
    """
    base_dir = os.path.dirname(__file__)
    dict_x = {}
    for root, dirs, files in os.walk(base_dir):
        if len(files) != 0:
            for i in files:
                stat_x = os.stat(os.path.join(root, i)).st_size
                dict_x[i] = stat_x
    return dict_x


result = {}
for i in dir_file():
    x = rounding(dir_file()[i])
    n = 0
    y = 0
    for j in dir_file():
        if dir_file()[j] == 0:
            y += 1
        elif rounding(dir_file()[j]) == x:
            n += 1
    result[0] = y
    result[rounding(dir_file()[i])] = n
sorted_result = dict(sorted(result.items(), key=lambda f: int(f[0])))
print(sorted_result)