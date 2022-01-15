import random


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    list_out = []
    while count > 0:
        list_out.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
        count -= 1
    return list_out


print(get_jokes(2))
print(get_jokes(10))


# Раскомментируйте для реализации подзаданий: документирование, флаг и именованные аргументы
def get_jokes_adv(count: int, reset: int = 0) -> list:
    """
    Возвращает список шуток в количестве count по умолчанию без повторений.
    Если при вызове функции добавить в качестве второго аргумента любое число отличное от 0, вернет результат get_jokes
    """
    if reset == 0:
        y = 0
        list_out = []
        list_x = []
        while count > 0:
            random_nouns = random.choice(nouns)
            random_adverbs = random.choice(adverbs)
            random_adjectives = random.choice(adjectives)
            if random_nouns not in list_x and random_adverbs not in list_x and random_adjectives not in list_x:
                list_out.append(f'{random_nouns} {random_adverbs} {random_adjectives}')
                list_x.append(random_nouns)
                list_x.append(random_adverbs)
                list_x.append(random_adjectives)
                y += 1
            else:
                count += 1
            if y >= len(nouns):
                print('Варианты без повторений закончились!')
                print(f'Максимальное количество вариантов шуток без повторений {len(list_out)}')
                break
            count -= 1
        return list_out
    else:
        return get_jokes(count)


print(get_jokes_adv(6, 1))
print(get_jokes_adv(6))