# 1. Реализовать вывод информации о промежутке времени в зависимости 
# от его продолжительности duration в секундах: до минуты: <s> сек; 
# до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * 
# в остальных случаях: <d> дн <h> час <m> мин <s> сек.

duration = [int(x) for x in input('Введите интервал времени или интервалы времени разделенные пробелами:').split()]

minute = 60
hour = 3600
day = 86400
week = 604800
month = 2629743
year = 31556926

for item in duration:
    if item < minute:
        print(item, 'sec')
    elif item < hour:
        print(item // minute, 'минут', item % minute, 'sec')
    elif item <day:
        hours = item // hour
        minutes = item % hour // minute
        sec = item % minute
        print(hours, 'часов', minutes, 'минут', sec, 'сек')
    else:
        days = item // day
        hours = item % day // hour
        minutes = item % day % hour // minute
        sec = item % minute
        print(days, 'днеей', hours, 'часов', minutes, 'минут', sec, 'сек')

    # сделал вплоть до лет если нужно раскомментировать удалите вышестоящий блок else

    # elif item < week:
    #     days = item // day
    #     hours = item % day // hour
    #     minutes = item % day % hour // minute
    #     sec = item % day % hour % minute
    #     print(days, 'днеей', hours, 'часов', minutes, 'минут', sec, 'сек')
    # elif item <month:
    #     weeks = item // week
    #     days = item % week // day
    #     hours = item % week % day // hour
    #     minutes = item % week % day % hour // minute
    #     sec = item % week % day % hour % minute
    #     print(weeks, 'недель', days, 'днеей', hours, 'часов', minutes, 'минут', sec, 'сек')
    # elif item < year:
    #     months = item // month
    #     weeks = item % month // week
    #     days = item % month % week // day
    #     hours = item % month % week % day // hour
    #     minutes = item % month % week % day % hour // minute
    #     sec = item % month % week % day % hour % minute
    #     print(months, 'месяцев', weeks, 'недель', days, 'днеей', hours, 'часов', minutes, 'минут', sec, 'сек')
    # else:
    #     years = item // year
    #     months = item % year // month
    #     weeks = item % year % month //week
    #     days = item % year % month % week // day
    #     hours = item % year % month % week // day
    #     minutes = item % year % month % week % day // minute
    #     sec = item % year % month % week % day % minutes
    #     print(years, 'лет', months, 'месяцев', weeks, 'недель', days, 'днеей', hours, 'часов', minutes, 'минут', sec, 'сек')
     
