import os


def conf(file_x):
    """
    :param file_x: .yaml
    :return: Диретории
    Создает директории и файлы согласно заданной структуре в файле конфигурации.
    """
    with open(file_x, 'r', encoding='utf-8') as fw:
        list_x = [i for i in fw]
        for i in list_x:
            x = len(i) - len(i.strip())
            base_dir = os.path.dirname(__file__)
            if x == 1:
                dir_name = i.strip()
                if not os.path.exists(dir_name):
                    os.mkdir(dir_name)
                else:
                    print(f'Дирректория {dir_name} существует!')
            elif 2 < x < 5:
                dir_name = i.strip()
                folder = os.path.join(base_dir, list_x[0].strip())
                folder_1 = os.path.join(folder, dir_name)
                try:
                    os.mkdir(folder_1)
                except FileExistsError:
                    print(f'Дирректория {dir_name} существует!')
            elif 5 < x < 8:
                dir_name = i.strip()
                folder_2 = os.path.join(folder_1, dir_name)
                if dir_name.endswith('.py') or dir_name.endswith('.html'):
                    my_file = open(folder_2, 'w')
                    my_file.close()
                else:
                    try:
                        os.mkdir(folder_2)
                    except FileExistsError:
                        print(f'Дирректория {dir_name} существует!')
            elif 8 < x < 11:
                dir_name = i.strip()
                folder_3 = os.path.join(folder_2, dir_name)
                if dir_name.endswith('.py') or dir_name.endswith('.html'):
                    my_file = open(folder_3, 'w')
                    my_file.close()
                else:
                    try:
                        os.mkdir(folder_3)
                    except FileExistsError:
                        print(f'Дирректория {dir_name} существует!')
            elif 11 < x < 14:
                dir_name = i.strip()
                folder_4 = os.path.join(folder_3, dir_name)
                if dir_name.endswith('.py') or dir_name.endswith('.html'):
                    my_file = open(folder_4, 'w')
                    my_file.close()
                else:
                    try:
                        os.mkdir(folder_4)
                    except FileExistsError:
                        print(f'Дирректория {dir_name} существует!')
            elif 15 < x < 18:
                dir_name = i.strip()
                folder_5 = os.path.join(folder_4, dir_name)
                if dir_name.endswith('.py') or dir_name.endswith('.html'):
                    my_file = open(folder_5, 'w')
                    my_file.close()
                else:
                    try:
                        os.mkdir(folder_5)
                    except FileExistsError:
                        print(f'Дирректория {dir_name} существует!')


if __name__ == '__main__':
    file_name = 'config_2.yaml'
    conf(file_name)
