from functools import wraps


def val_checker(req=lambda x: x):
    def val_wrapper(func):
        @wraps(func)
        def wrapper(*args):
            for i in args:
                if type(i) == int:
                    int(i)
                else:
                    raise ValueError(f'wrong val {i}')
            return func(*args)
        return wrapper
    return val_wrapper


@val_checker()  # не забудьте про аргумент-функцию
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube('ss'))