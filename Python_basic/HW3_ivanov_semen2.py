# Задание 1. Есть list с данными lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
# Напишите механизм, который формирует новый list (например lst2), который содержит только переменные-строки
# которые есть в lst1

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for elements in lst1:
    if isinstance(elements, str):
        lst2.append(elements)
print(lst2)

# Задание 2. Ввести из консоли строку. Определить количество слов в этой строке, которые начинаются на букву "а"
# (учтите, что слова могут начинаться с большой буквы).

my_str = input(str('Пожалуйста введите текст: ')).lower()
my_list = my_str.split()
a_word_counter = int()

for word in my_list:
    if word.startswith('a'):
        a_word_counter += 1
print(a_word_counter)

# Задание 3.* Вывести пользователю приветствие ('Hello!'). Спросить у пользователя, хочет ли он повторно его увидеть
# этот текст?. Если пользователь введет Y - повторить приветствие. После каждого приветствия повторять вопрос. Если
# если пользователь введет N - прекратить спрашивать. Если пользователь ввел не Y или N - попросить ввести именно Y
# или N, переспрашивать пока не введет Y или N и по результату принимать решение повторять или нет.

while True:
    print('Hello')
    answer = input('Do you want to see this message again? Y/N : ')
    if answer.lower() != 'n':
        while answer.lower() not in ('y', 'n'):
            answer = input('Only Y or N available! Repeat please : ')
        if answer.lower() == 'n':
            break
        continue
    break
