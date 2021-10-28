

spisok = []

for i in range (1, 1000):
    if i**3 % 2 != 0:
        spisok.append(i**3)


for i in spisok:
    x = len(str(i))
    num_sum = 0
    z = i
    while x > 0:
        y = z % 10
        num_sum += y
        x -= 1
        z //= 10
    if num_sum % 7 == 0:
        print('Сумма числа', i, 'равна', num_sum, 'результат деления на 7 ->', num_sum/7)


print('\n\n добавили к каждому числу из списка 17. * Без создания доп. списка\n\n')


for i in spisok:
    i += 17
    x = len(str(i))
    num_sum = 0
    z = i
    while x > 0:
        y = z % 10
        num_sum += y
        x -= 1
        z //= 10
    if num_sum % 7 == 0:
        print('Сумма числа', i, 'равна', num_sum, 'результат деления на 7 ->', num_sum/7)


