import time
from datetime import datetime

# Напишите класс Point - точка на координатной плоскости, у которой есть аргументы, отвечающие
# за коордиату Х и координату Y. Реализуйте передачу в X и Y только числовых значений. Добавьте
# метод __str__, который бы отдавал информацию о точке в формате "Point with x: 10, y: 20"


class DescriptorXY:
    _val = 0

    def __set__(self, inst, value):
        if not isinstance(value, (int, float)):
            print('Only integers or float allowed!')
            raise Exception
        self._val = value

    def __get__(self, *args, **kwargs):
        return self._val


class Point:
    x = DescriptorXY()
    y = DescriptorXY()

    def __init__(self, a, b):
        self.x = a
        self.y = b

    def __str__(self):
        return f'Point with x: {self.x}, y: {self.y}'


point1 = Point(6, 7)
print(point1.__str__())

point2 = Point(10.1, 5.5)
print(point2.__str__())


print('-'*100)

# Напишите декоратор, измеряющий время выполнения функции.


def funcTimeCounter(yourFunc):  # принимаем нашу функцию в декоратор в качестве аргумента

    def funcWrapper(*args):  # в wrapper функцию-обертку передаем аргументы нашей функции
        startTimer = time.time()  # старт таймера
        yourFunc(*args)  # выполняем нашу функцию
        endTimer = time.time()  # останавливаем таймер
        print(f'-----> Elapsed time: {endTimer - startTimer} seconds. <----')  # принтуем результат
        return yourFunc(*args)

    return funcWrapper


@funcTimeCounter
def fiba(k):
    fstFiba = 1
    scndFiba = 1
    k = k - 2
    while k > 0:
        fstFiba, scndFiba = scndFiba, fstFiba + scndFiba
        k -= 1
    return scndFiba


print(fiba(99999))


print('-'*100)

# 3* Модифицируйте декоратор таким образом чтобы декоратор вместе с ответом функции возвращал строку,
# содержащую информацию о затраченном на выполнение времени. Формат возвращаемого времеени- H-MM-SS-MS.


def modFuncTimeCounter(yourFunc):

    def funcWrapper2(*args):
        startTimer = datetime.now()
        wrappedFunc = yourFunc(*args)
        endTimer = datetime.now()
        res = f'--> Elapsed time: {endTimer - startTimer} seconds. <--'
        return res, wrappedFunc

    return funcWrapper2


@modFuncTimeCounter
def fiba(k):
    fstFiba = 1
    scndFiba = 1
    k = k - 2
    while k > 0:
        fstFiba, scndFiba = scndFiba, fstFiba + scndFiba
        k -= 1
    return scndFiba


print(fiba(9000))
print(type(fiba(9000)[0]))
