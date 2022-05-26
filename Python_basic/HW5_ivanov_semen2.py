# Написать функцию, принимающую один аргумент. Функция должна вывести на экран тип данных этого аргумента
# (используйте type)

def my_function(a):
    print(type(a))


my_function(a=1234)
my_function(a="fdsfsf")
my_function(a=[3, 2, 3])
my_function(a=False)


# Написать функцию, принимающую два аргумента. Функция должна :
# - если оба аргумента относятся к числовым типам - вернуть их произведение,
# - если к строкам - соединить в одну строку и вернуть,
# - если первый строка, а второй нет - вернуть словарь (dict), в котором ключ - первый аргумент, значение - второй
# в любом другом случае вернуть кортеж (tuple) из аргументов

def my_function2(a, b):
    if type(a) == int and type(b) == int:
        return a * b
    elif type(a) == str and type(b) == str:
        return a + b
    elif type(a) == str and type(b) != str:
        return {a: b}
    else:
        return (a, b)


print(my_function2(a=3, b=6))
print(my_function2(a='yello ', b='world'))
print(my_function2(a="world", b=3))
print(my_function2(a=3.3, b=3.6))

# Дан словарь продавцов и цен на какой то товар у разных продавцов: { ‘citrus’: 47.999, ‘istudio’ 42.999,
# ‘moyo’: 49.999, ‘royal-service’: 37.245, ‘buy.ua’: 38.324, ‘g-store’: 37.166, ‘ipartner’: 38.988, ‘sota’: 37.720 }.
# Написать функцию возвращающую список имен продавцов, чьи цены попадают в диапазон. Диапазон определяется как начало
# и конец. Функция должна принимать словарь с ценами, начало и конец диапазона и возвращать список (list) имен.

dct = {
    'citrus': 47.999,
    'istudio': 42.999,
    'moyo': 49.999,
    'royal-service': 37.245,
    'buy.ua': 38.324,
    'g-store': 37.166,
    'ipartner': 38.988,
    'sota': 37.720}


def stores(dct, x, y):
    lst = []
    for key, value in dct.items():
        if x <= value <= y:
            lst.append(key)
    return print(lst)


x = float(input('Введите начальную цену: '))
y = float(input('Введите конечную цену: '))
stores(dct, x, y)

# * Пользователь вводит строку произвольной длины. Написать функцию, которая должна вернуть словарь
# следующего содержания: ключ - количество букв в слове, значение - список слов с таким количеством букв.
# Отдельным ключем, например "0", записать количество пробелов. Отдельным ключем, например "punctuation",
# записать все уникальные знаки препинания, которые есть в тексте. Например:
# {
# "0": количество пробелов в строке
# "1": list слов, состоящих из одной буквы
# "2": list слов, состоящих из двух букв
# "3": list слов, состоящих из трех букв
# и т.д  для всех возможных вариантов длины слова в переденной строке...
# "punctuation" : tuple уникальных знаков препинания
# }

str1 = 'Пользователь Пользователю a ? вводит строку ! количество ,'


def my_slo_creator(str1):
    dct1 = {}
    set_str1 = set(str1)
    znaki = {'.', ',', '!', '?', '-', ':', ';'}
    dct1.update({(str1.count(' ')): ['количество пробелов в строке']})
    dct1.update({'punctuation': tuple(set_str1.intersection(znaki))})
    for i in str1.split():
        if i not in znaki:
            key = len(i)
            dct1.setdefault(key, [])
            dct1[key].append(i)
    for key2, value in dct1.items():
        print("{0}: {1}".format(key2, value))
    return dct1


my_slo_creator(str1)

