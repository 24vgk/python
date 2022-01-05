

def num_translate(value: str) -> str:
    """переводит числительное с английского на русский """
    ru = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
    en = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    for ru, en in zip(ru, en):
        if value == en:
            str_out = ru
            return str_out


print(num_translate("one"))
print(num_translate("eight"))