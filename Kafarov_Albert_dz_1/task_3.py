# 3.Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов». 
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:

for i in range(1,101):
    if 11 < i < 15:
        print(i, 'процентов')
    elif i % 10 == 1 and i != 11:
        print(i, 'процент')
    elif 1 < i < 5 or 1 < i % 10 < 5:
        print(i, 'процента')
    elif 4 < i < 11 or 4 < i % 10 < 11:
        print(i, 'процентов')
    else:
        print(i, 'процентов')


