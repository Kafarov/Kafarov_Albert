# 3. * (вместо задачи 2) Решить задачу 2 не создавая новый список
# (как говорят, in place). Эта задача намного серьёзнее, чем может сначала показаться.


lst = ['в', '5', 'часов', '17', 'минут',
       'температура', 'воздуха', 'была', '+5', 'градусов']

lst_iter = iter(lst)

count = 0

for item in lst_iter:
    if item.isdigit():
        lst.remove(item)
        item = f'{int(item):02}'
        lst.insert(count, '"')
        lst.insert(count+1, item)
        lst.insert(count+2, '"')
        count += 2
        next(lst_iter)
    elif item.strip('+-').isdigit():
        lst.remove(item)
        item = item[0] + f'{int(item):02}'
        lst.insert(count, '"')
        lst.insert(count+1, item)
        lst.insert(count+2, '"')
        count += 2
        next(lst_iter)
    else:
        count += 1

print(' '.join(lst))
