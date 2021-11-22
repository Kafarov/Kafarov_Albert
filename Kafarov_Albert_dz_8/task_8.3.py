from functools import wraps


def type_logger(callback):
    @wraps(callback)
    def wrapper(*args):
        for el in args:
            print(f'{callback.__name__}({el} : {type(el)})')
        a = callback(*args)
        return a
    return wrapper


@type_logger
def calc_cube(*args):
    for x in args:
        print(x**3)


a = calc_cube(5, 6)
