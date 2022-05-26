# Дан list произвольных чисел (напр [11, 77, 4, 22, 0, 56, 5, 95, 7, 87, 13, 45, 67, 44,]).
# Написать программу, которая удалит из него все числа, которые меньше 18 и больше 81.
# учтите, что это должен быть именно исходный лист (с тем же id) а не новый
# import Imports as Imports

import copy

lst = [1, 2, 3, 19, 4, 4, 5, 20, 6, 6, 8, 9, 9]
for x in copy.deepcopy(lst):
    if x < 18 or x > 81:
        lst.remove(x)
print(lst)

# "Искусственный интеллект". Пользователь вводит строку произвольного содержания. Программа должна сообщить:
# "It's phone number" если строка это телефонный номер ("+" и 12 цифр, напр +380631112233)
# "It's name" если строка это ФИО (имя и инициалы, например Ivanov A. B.)

str1 = input()
str3 = str1.split(' ')

if str1[0] == '+' and int(str1[1:12]) and len(str1) == 13:
    print('It\'s phone number:', str1)
elif len(str3) == 3 and str3[1][1] == '.' and str3[2][1] == '.' and str(str3[0]):
    print('It\'s a name:', str1)
else:
    print(str1)

#
# # 3.*  Пользователь вводит строку произвольного содержания. Найти в строке самое длинное слово, в котором
# # присутствуют подряд две согласные буквы. Если в строке присутствует слово с тремя согласными
# # буквами подряд - вывести его на экран
#
text = 'Смотрите все результаты поиска по вашему заппросу и правилааааа собблюдайте правилаааа безопасност прво'
consonants_symbols = ('б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ш', 'щ')
very_long_word = str()
for item in text.split():
    counter = 0
    for s in item:
        if s.lower() in consonants_symbols:
            counter += 1
        else:
            counter = 0
            continue
        if counter == 2 and len(item) > len(very_long_word):
            very_long_word = item
        elif counter == 3:
            print(f'Слово с тремя согласными: {item} ')
print(f'Самое длинное слово с двумя согласными: {very_long_word}')
