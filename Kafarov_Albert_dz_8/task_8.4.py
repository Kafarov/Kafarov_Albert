from functools import wraps


def val_checker(callback):
    @wraps(callback)
    def wrapper(x):
        try:
            if (lambda i: i < 0)(x):
                raise ValueError
        except ValueError:
            msg = f'Некорректное знвчение {x}'
            exit(ValueError(msg))
        a = callback(x)
        return a
    return wrapper


@val_checker
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
