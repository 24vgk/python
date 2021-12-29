

def search_sing(x):
    if x[0] in '+-':
        return x[0]


def convert_list_in_str(list_in: list) -> str:
    i = 0
    while i < len(list_in):
        changes = search_sing(list_in[i])
        if list_in[i].isdigit() or (changes and list_in[i][1:].isdigit()):
            if changes:
                list_in[i] = changes + list_in[i][1:].zfill(2)
            else:
                list_in[i] = list_in[i].zfill(2)
            list_in.insert(i, '"')
            list_in.insert(i + 2, '"')
            i += 2
        i += 1
    str_out = ' '.join(list_in)
    return str_out


if __name__ == '__main__':
    my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
    result = convert_list_in_str(my_list)
    print(result)
