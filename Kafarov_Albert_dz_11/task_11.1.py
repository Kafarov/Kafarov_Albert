import re
from datetime import datetime


class Date:

    def __init__(self, date):
        self.date = date

    @classmethod
    def converter(cls, date):
        pattern = re.compile(r'(\d{2})[-. ](\d{2})[-. ](\d{4})')
        result_iter = pattern.finditer(date)
        day = 0
        month = 0
        year = 0
        for i in result_iter:
            day = int(i.group(1))
            month = int(i.group(2))
            year = int(i.group(3))
        valid = cls.validator(day, month, year)
        if valid is not None:
            print(valid)

    @staticmethod
    def validator(day, month, year):
        date = f'{day}/{month}/{year}'
        try:
            valid_date = datetime.strptime(date, '%d/%m/%Y').date()
            return valid_date
        except ValueError:
            print('invalid date')


d_1 = Date('04-12-2021')

d_1.converter('04-12-2021')
