def is_odd(x):
    for i in range(1, x+1, 2):
        yield print(i)


odd = is_odd(15)
next(odd)
next(odd)
next(odd)

