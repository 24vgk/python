import time


def get_uniq_numbers(src: list):
    x = set()
    y = set()
    for i in src:
        if i in x:
            y.discard(i)
        else:
            y.add(i)
        x.add(i)
    return [j for j in src if j in y]


start = time.time()
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))
end = time.time()
print(end - start)


# А так я решил в ЛОБ)))
# def get_uniq_numbers(src: list):
#     return [i for i in src if src.count(i) == 1]
#
#
# start = time.time()
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# print(*get_uniq_numbers(src))
# end = time.time()
# print(end - start)