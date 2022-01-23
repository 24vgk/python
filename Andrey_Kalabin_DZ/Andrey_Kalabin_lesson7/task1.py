import os


def conf(file_x):
    """
    :param file_x: .yaml
    :return: Диретории
    Создает директории согласно заданной структуре в файле конфигурации.
    """
    with open(file_x, 'r', encoding='utf-8') as fw:
        list_x = [i for i in fw]
        for i in list_x:
            x = len(i) - len(i.strip())
            if x == 1:
                base_dir = os.path.dirname(__file__)
                dir_name = i.strip()
                if not os.path.exists(dir_name):
                    os.mkdir(dir_name)
                else:
                    print(f'Дирректория {dir_name} существует!')
            elif 2 < x < 5:
                dir_name = i.strip()
                folder = os.path.join(base_dir, list_x[0].strip())
                folder_x = os.path.join(folder, dir_name)
                try:
                    os.mkdir(folder_x)
                except FileExistsError:
                    print(f'Дирректория {dir_name} существует!')


if __name__ == '__main__':
    file_name = 'config.yaml'
    conf(file_name)
