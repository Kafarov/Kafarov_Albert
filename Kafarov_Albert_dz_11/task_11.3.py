class ValidNum:
    @staticmethod
    def validator(num):
        try:
            float(num)
            return float(num)
        except ValueError:
            return False


lst = []
while True:
    num = input('Введите число: ')
    valid_num = ValidNum.validator(num)
    if num == 'stop':
        print(lst)
        break
    if valid_num is False:
        print('Некорректное число')
        continue
    else:
        lst.append(valid_num)
