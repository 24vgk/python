n = 15
gen_x = (result for result in range(1, n + 1, 2))


if __name__ == '__main__':
    for _ in range(1, n + 1, 2):
        print(next(gen_x))