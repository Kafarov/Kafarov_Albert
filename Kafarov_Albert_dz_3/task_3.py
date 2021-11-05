def thesaurus(x):
    for i in x:
        staff_name.setdefault(i[0][0], []).append(i)
    return staff_name

staff_name ={}

print(thesaurus(input('Введите имена сотрудников через пробел:\n').split()))


# inputs = [a.strip('",') for a in input('Введите имена сотрудников: ').split()] 
# print(thesaurus(inputs))