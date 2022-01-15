

def transform_string(number: int) -> str:
    total = number % 10
    if number == 1 or number > 11 and total == 1:
        return (f'{number} процент')
    elif number > 1 and number < 5 or number > 20 and total > 1 and total < 5:
        result = (f'{number} процента')
        return result
    else:
        result = (f'{number} процентов')
        return result


if __name__ == '__main__':
    for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
        print(transform_string(n))