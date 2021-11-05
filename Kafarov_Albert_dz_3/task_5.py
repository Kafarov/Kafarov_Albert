import random

def  get_jokes(x):
    a =0
    while a <x:
        joke = random.choice(nouns) + ' ' + random.choice(adverbs) + ' ' + random.choice(adjectives)
        a += 1
        print(joke)
    return

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

inputs = get_jokes(int(input('Введите количество шуток:')))