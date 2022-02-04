import sys
import time

def get_numbers(src: list):
    """
    на мой взгляд самое оптимальное решение
    """
    return (src[i] for i in range(len(src)) if src[i] > src[i - 1] and i != 0)

start = time.time()
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = get_numbers(src)
print(*get_numbers(src))
print(sys.getsizeof(result), 'объем памяти списка')
end = time.time()
print(end - start, 'Затраченное время')

# def get_numbers1(src: list):
#     """
#     Решаем через генератор, но проблема в том что мы не знаем
#     сколько нужных чисел в списке и значит закончим выполнение программы ошибкой
#     """
#     for i in range(len(src)):
#         if src[i] > src[i - 1] and i != 0:
#             yield src[i]
#
#
#
# start = time.time()
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# generator = get_numbers1(src)
# print(sys.getsizeof(generator), 'объем памяти генератора')
# for _ in range(6):
#     print(next(generator))
# end = time.time()
# print(end - start, 'Затраченное время')