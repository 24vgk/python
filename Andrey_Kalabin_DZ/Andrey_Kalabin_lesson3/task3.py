

def thesaurus(*args) -> dict:
    dict_out = {}
    for i in args:
        dict_out[i[0]] = list(set(filter(lambda el: el.startswith(i[0]), args)))
    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Иван"))