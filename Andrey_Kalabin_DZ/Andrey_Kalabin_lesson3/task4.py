

def name_x(list_name):
    letter = list_name.split()
    return letter[1][0]


def guide(list_name):
    result_dict = {}
    letter_name = []
    for j in list_name:
        letter_name.append(name_x(j))
    for k in set(letter_name):
        auxiliary_list = []
        two_dict = {}
        for i in list_name:
            y = i.index(' ')
            if k == i[y + 1]:
                auxiliary_list.append(i)
            if len(list(filter(lambda el: el.startswith(i[0]), auxiliary_list))) != 0:
                two_dict[i[0]] = list(filter(lambda el: el.startswith(i[0]), set(auxiliary_list)))
        result_dict[k] = two_dict
    return result_dict


thesaurus_list = (
                    "Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева",
                    "Андрей Калабин", "Виктория Калабина", "Анна Савельева"
                  )
print(guide(thesaurus_list))
