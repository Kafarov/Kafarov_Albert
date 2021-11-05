def num_translate(x):
    return translate_lst.get(x)


translate_lst = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

print(num_translate(input('Введите число от одного до десяти:')))
