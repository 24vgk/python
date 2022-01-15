

def convert_name_extract(list_in: list) -> list:
    list_out = []
    for item, name in zip(list_in, [s[s.rindex(' ') + 1:].capitalize() for s in list_in]):
        list_in[list_in.index(item)] = f"{item[:item.rindex(' ')]} {name}"
        list_out.append(f'Привет {name}!')
    return list_out


if __name__ == '__main__':
    my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
    result = convert_name_extract(my_list)
    print(result)