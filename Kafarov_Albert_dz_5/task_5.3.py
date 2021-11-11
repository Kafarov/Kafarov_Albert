

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
if len(tutors) > len(klasses):
    (klasses.append(None) for el in range(len(tutors) - len(klasses)))

g = ((a, b) for a, b in zip((tutors), klasses))

print(next(g))
print(next(g))
print(next(g))
