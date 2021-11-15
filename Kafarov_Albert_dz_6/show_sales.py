import sys
import pandas as pd


def show_sales(*args):
    with open('bakery.csv', 'r', encoding='utf-8') as bakery:
        if len(args) > 1:
            data = pd.read_csv(bakery, skiprows=args[0], nrows=args[1]-args[0])
            print(data)
        else:
            data = pd.read_csv(bakery, skiprows=args[0])
            print(data)


i = tuple(int(i) for i in sys.argv[1:])

if len(i) == 1:
    show_sales(i[0])
elif len(i) == 0:
    show_sales(0)
else:
    show_sales(i[0], i[1])
