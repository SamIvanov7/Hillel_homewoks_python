import re
# Напишите функцию для парсинга номерных знаков автомоблей Украины (стандарты - AА1234BB, 12 123-45AB, a12345BC)
# с помощью регулярных выражений. Функция принимает строку и возвращает None если строка не является номерным знаком.
# Если вся сторка является номерным знаком - функция возвращает саму строку.
# Создайте публичный репозиторий на GitLab или GitHub. Сохраните отдельной веткой (пусть будет ветка HW13)


my_str = 'BillAA0001BXGa5&&BH0741BE&&&aajhkfajgferrgа12367BEghjfdjfrejjkBH6578AXghkrgheAE5436TXke7876 \ ' \
         'dBE1234AXggddfdssю67854BT4875fafsafsa12 123-22XTfdsfs'


def numberParser(my_str):
    tpl = '(?!0{2})\d{2}\s(?!0{3})\d{3}-(?!0{2})\d{2}[ABCEHIKMOPTX]{2}|' \
           '[ABCEHIKMOPTX]{2}(?!0{4})\d{4}[ABCEHIKMOPTX]{2}|' \
           '[а-я]{1}(?!0{5})\d{5}[ABCEHIKMOPTX]{2}'
    for match in re.findall(tpl, my_str):
        if match == 0:
            return None
        else:
            return re.findall(tpl, my_str)


print(numberParser(my_str))
