import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    result = {}
    with open(path_users_file, 'r', encoding='utf-8') as fw, open(path_hobby_file, 'r', encoding='utf-8') as fr:
        x = fw.readlines()
        y = fr.readlines()
        if len(x) < len(y):
            sys.exit(1)
        for i in range(max(len(x), len(y))):
            name = x[i].strip().split(',')
            try:
                hobby = y[i].strip().split(',')
                result[' '.join(name)] = hobby
            except:
                hobby = None
                result[' '.join(name)] = hobby
        return result


dict_out = prepare_dataset('users.csv', 'hobby.csv')
print(dict_out)
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)