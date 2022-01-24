import os
import shutil


def way(adr_list, dir):
    dir_x = {}
    list_x = []
    for i in adr_list:
        if i == dir_name:
            continue
        else:
            folder = dir + '/' + i
            folder1 = os.listdir(folder)
            if dir_name in folder1:
                folder2 = folder + '/' + dir_name
                list_x += os.listdir(folder2)
                dir_x[''.join(os.listdir(folder2))] = folder2
    return dir_x


dir_name = 'templates'
base_dir = os.path.dirname(__file__)
x = os.listdir(base_dir)
for i in x:
    if i == 'my_project':
        base_dir += '/' + i
x = os.listdir(base_dir)
folder = os.path.join(base_dir, dir_name)
try:
    os.mkdir(folder)
except FileExistsError:
    print(f'Дирректория {dir_name} существует!')
result = way(x, base_dir)
for j in result:
    folder_1 = folder + '/' + j
    try:
        os.mkdir(folder_1)
    except FileExistsError:
        print(f'Дирректория {folder_1} существует!')
    y = os.listdir(result[j] + '/' + j)
    adr_file = result[j] + '/' + j
    for n in y:
        shutil.copy2(os.path.join(adr_file, n),  os.path.join(folder_1, n))


