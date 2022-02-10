from functools import wraps


def type_logger(func):

    @wraps(func)
    def wrapper(*args):
        result = [f'{func.__name__}({i}:{type(i)})' for i in args]
        return ' \n'.join(result)
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5, 9)
print(a)
