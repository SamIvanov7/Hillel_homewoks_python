# В отдельном файле (пусть будет lib.py) написать функцию, которая требует от пользователя ответить
# да или нет ( Y\N ) и воз вращает True\False в зависимости от того, что он ввел. В основном файле
# (пусть будет main_file.py) попросить пользователя ввести с клавиатуры строку и вывести ее на экран.
# Используя импортированную из lib.py функцию спросить у пользователя, хочет ли он повторить операцию (Y/N).
# Повторять пока пользователь отвечает Y и прекратить когда пользователь скажет N.

from lib import answer

while True:
    text1 = input('Please enter some text here: ')
    if answer() is False:
        break

# Пишем игру ) Программа выбирает из диапазона чисел (1-100) случайное число и предлагает пользователю его
# угадать. Пользователь вводит число. Если пользователь не угадал - предлагает пользователю угадать еще раз,
# пока он не угадает. Если угадал - спрашивает хочет ли он повторить игру (Y/N). Если Y - повторить. N - Прекратить

from random import randint

print('Hello. Let\'s play game. ')


def type_checker(a) -> bool:
    try:
        a = int(a)
    except ValueError:
        print('Please, input only integers!')
        exit()
    except TypeError:
        print('Please, input only integers!')
        exit()
    return a


def value_checker(b: int) -> int:
    if b not in range(1, 100):
        print('Error! Please check your playing number\'s value')
        exit()
    else:
        return b


def game():
    rand_numb = randint(1, 100)
    while True:
        my_numb = input('Please enter the number between 1 and 100: ')
        my_numb = type_checker(my_numb)
        my_numb = value_checker(my_numb)
        if my_numb == rand_numb:
            print("Congratulations! You win!!!")
        elif my_numb != rand_numb:
            print('You loose, game over!')
        play_again = input("One more time?(yes or no) : ")
        if play_again == "yes":
            continue
        elif play_again == "no":
            exit()
        else:
            print("Unknown command")
            break


game()


# 3* Добавить в задание 2 счетчик попыток и диапазон чисел (начало и конец). Пользователь вводит количество
# попыток, за которые он может угадать число, пользователь вводит начало и конец диапазона. На каждом шаге
# угадывания числа сообщайте пользователю сколько попыток у него осталось. Если пользователь не смог угадать за
# отведенное количество попыток сообщить ему об окончании (Looser!).

from random import randint

print('Hello. Let\'s play game. ')

counter = 0


def main():
    global counter
    counter_range = input('Choose how many trials do yo want to have. Between 1 and 10: ')
    fstNumber = input('Enter Min number of range between 1 and 100 ')
    scndNumber = input('Enter Max number of range between 1 and 100 ')
    my_numb = input('Please enter the number in range from 1 to 100 to play: ')

    counter_range = type_checker(counter_range)
    my_numb = type_checker(my_numb)
    fstNumber = type_checker(fstNumber)
    scndNumber = type_checker(scndNumber)
    counter_range, my_numb, fstNumber, scndNumber = value_checker(counter_range, my_numb, fstNumber, scndNumber)

    rand_numb = randint(fstNumber, scndNumber)
    operation_counter(my_numb, rand_numb, counter, counter_range)

    play_again = input("One more time?(yes or no) : ")
    if play_again == "yes":
        main()
    elif play_again == "no":
        exit()
    else:
        print("Unknown command")
    return True


def type_checker(a) -> bool:
    try:
        a = int(a)
    except ValueError:
        print('Please, input only integers!')
        exit()
    except TypeError:
        print('Please, input only integers!')
        exit()
    return a


def value_checker(counter_range, my_numb, fstNumber, scndNumber):
    if counter_range not in range(1, 10):
        print('Error! Please check your number of tries value')
        exit()
    if my_numb not in range(1, 100) or my_numb < fstNumber or my_numb > scndNumber:
        print('Error! Please check your playing number\'s value')
        exit()
    if fstNumber not in range(1, 100) or fstNumber >= scndNumber:
        print('Error! Please check your Min number\'s value')
        exit()
    if scndNumber not in range(1, 100):
        print('Error! Please check your Max number\'s value')
        exit()
    return counter_range, my_numb, fstNumber, scndNumber


def operation_counter(a, b, c, d):
    while True:
        a = type_checker(a)
        if a == b:
            print("Congratulations! You win!!!")
            break
        if a != b:
            c += 1
            if c == d:
                print('Hey, Looser!!!! Your tries are over! Good Bye!')
                break
            elif (d - c) == 0:
                print('Last trial !!! Be careful!!!')
                a = input('Please enter a number: ')
                continue
            else:
                print(f'{d - c} trials left')
                a = input('Please enter a number: ')
                continue
    return a, b, c, d


main()


# 4** Добавить в задание 2 вывод сообщения-подсказки. Если пользователь ввел число, и не угадал -
# сообщать: "Холодно" если разница между загаданным и введенным числами больше 10, "Тепло" - если от
# 5 до 10 и "Горячо" если от 4 до 1.

from random import randint

print('Hello. Let\'s play game. ')

counter = 0


def main():
    global counter
    counter_range = input('Choose how many trials do yo want to have. Between 1 and 10: ')
    fstNumber = input('Enter Min number of range between 1 and 100 ')
    scndNumber = input('Enter Max number of range between 1 and 100 ')
    my_numb = input('Please enter the number in range from 1 to 100 to play: ')

    counter_range = type_checker(counter_range)
    my_numb = type_checker(my_numb)
    fstNumber = type_checker(fstNumber)
    scndNumber = type_checker(scndNumber)
    counter_range, my_numb, fstNumber, scndNumber = value_checker(counter_range, my_numb, fstNumber, scndNumber)

    rand_numb = randint(fstNumber, scndNumber)
    cold_hot(my_numb, rand_numb, counter, counter_range)

    play_again = input("One more time?(yes or no) : ")
    if play_again == "yes":
        main()
    elif play_again == "no":
        exit()
    else:
        print("Unknown command")
    return True


def type_checker(a) -> bool:
    try:
        a = int(a)
    except ValueError:
        print('Please, input only integers!')
        exit()
    except TypeError:
        print('Please, input only integers!')
        exit()
    return a


def value_checker(counter_range, my_numb, fstNumber, scndNumber):
    if counter_range not in range(1, 10):
        print('Error! Please check your number of tries value')
        exit()
    if my_numb not in range(1, 100) or my_numb < fstNumber or my_numb > scndNumber:
        print('Error! Please check your playing number\'s value')
        exit()
    if fstNumber not in range(1, 100) or fstNumber >= scndNumber:
        print('Error! Please check your Min number\'s value')
        exit()
    if scndNumber not in range(1, 100):
        print('Error! Please check your Max number\'s value')
        exit()
    return counter_range, my_numb, fstNumber, scndNumber


def cold_hot(a, b, c, d):
    while True:
        a = type_checker(a)
        if a == b:
            print('Winner Winner! Chicken dinner!)')
            break
        if a != b:
            c += 1
            print(f'{d - c} trials left')
            if c == d:
                print('Hey, Looser!!!! Your tries are over! Good Bye!')
                break
            if ((a - b) >= 10) or ((b - a) >= 10):
                print('Too cold!!')
                a = input('Please enter a number: ')
                continue
            elif (5 <= (a - b) < 10) or (5 <= (b - a) < 10):
                print('Warmer...))')
                a = input('Please enter a number: ')
                continue
            elif (1 <= (a - b) < 5) or (1 <= (b - a) < 5):
                print('Hot!!!')
                a = input('Please enter a number: ')
                continue
    return a, b, c, d


main()
