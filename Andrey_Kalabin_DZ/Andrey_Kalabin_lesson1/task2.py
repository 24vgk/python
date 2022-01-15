

def sum_list_1(dataset: list) -> int:
    sum_numbers_1 = 0
    for i_a in dataset:
        sum_numbers_a = 0
        for j in str(i_a):
            sum_numbers_a += int(j)
        if sum_numbers_a % 7 == 0:
            sum_numbers_1 += i_a
    return sum_numbers_1


def sum_list_2(dataset: list) -> int:
    sum_numbers_2 = 0
    for i_b in dataset:
        sum_numbers_b = 0
        n_b = i_b + 17
        while n_b != 0:
            sum_numbers_b += n_b % 10
            n_b = n_b // 10
        if sum_numbers_b % 7 == 0:
            sum_numbers_2 += i_b + 17
    return sum_numbers_2


if __name__ == '__main__':
    my_list = [i**3 for i in range(1, 1001) if i % 2 != 0]
    result_1 = sum_list_1(my_list)
    print(result_1)
    result_2 = sum_list_2(my_list)
    print(result_2)