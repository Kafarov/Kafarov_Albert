import csv
import sys


def add_sale(x):
    with open('bakery.csv', 'a', newline='', encoding='utf-8') as bakery:
        csv_writer = csv.writer(bakery, dialect='excel')
        csv_writer.writerow(x)


add_sale(sys.argv[1:])
