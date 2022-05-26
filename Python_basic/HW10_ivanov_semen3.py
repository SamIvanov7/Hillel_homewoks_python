# 1. Доработайте класс Line из занятия. Обеспечьте передачу в него только точек при создании обьекта
# линия. Добавьте проверку на то, что точки не совпадают, чтобы не получилась линия нулевой длины.
# Переопределите метод __str__ так, чтобы он отдавал информацию о координатах
# и длину ("line (0, 0) - (3, 4) with length 5")

class Point:
    x = None
    y = None

    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise Exception
        self.x, self.y = x, y

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.x == other.x and self.y == other.y


class Line:
    p1 = None
    p2 = None

    def __init__(self, a, b):
        if not isinstance(a, Point) or not isinstance(b, Point):
            raise Exception
        if a.__eq__(b) is True:
            raise Exception
        self.p1, self.p2 = a, b

    def length(self):
        return ((self.p1.x - self.p2.x)**2 + (self.p1.y - self.p2.y)**2)**0.5

    def __str__(self):
        return f'line ({self.p1.x}, {self.p1.y}) - ({self.p2.x}, {self.p2.y}) with length {self.length()}'


p1 = Point(3, 4.7)
p2 = Point(2, 6)
l1 = Line(p1, p2)

print(l1.__str__())

print('*'*70)

# 2. Доработайте класс Triangle. Обеспечьте передачу в него только точек при создании обьекта треугоьлник.
# Добавьте метод вычисления собственной площади по формуле Герона

# 3. * Доработайте класс Triangle. Добавьте итератор сторон - метод sides(), добавьте вычисляемый атрибут - периметр,
# добавьте вычисляемый атрибут - площадь


class Triangle:
    p1 = None
    p2 = None
    p3 = None
    sideIndex = 0

    def __init__(self, a, b, c):
        if not isinstance(a, Point) or not isinstance(b, Point) or not isinstance(c, Point):
            raise Exception
        self.p1, self.p2, self.p3 = a, b, c
        self.l1 = Line(a, b)
        self.l2 = Line(b, c)
        self.l3 = Line(a, c)

    # Итератор сторон

    def __iter__(self):  # первый способ.
        self.sideIndex = 0
        return self

    def __next__(self):
        print(f'Сторона №{self.sideIndex} треугольника')
        if self.sideIndex > 2:
            raise StopIteration
        side = (self.l1, self.l2, self.l3)
        self.sideIndex += 1
        print(side[self.sideIndex - 1])

    def sides(self):  # второй способ
        side = (self.l1, self.l2, self.l3)
        for i in side:
            print(i)
        return side

    @property
    def perimetr(self):
        return self.l1.length() + self.l2.length() + self.l3.length()

    @property
    def square(self):  # вычисляется по формуле Герона(Задание 2)
        halfPer = self.perimetr / 2.0  # Полупериметр
        sL1, sL2, sL3 = self.l1.length(), self.l2.length(), self.l3.length()
        squareGeron = (halfPer * (halfPer - sL1) * (halfPer - sL2) * (halfPer - sL3)) ** 0.5
        return squareGeron


p1 = Point(15, 4)
p2 = Point(2, 62)
p3 = Point(7, 9)
triangle1 = Triangle(p1, p2, p3)

print(f'периметр  = {triangle1.perimetr}')  # вычисляемый атрибут периметр
print(f'Площадь = {triangle1.square}')  # вычисляемый атрибут площадь

print('*'*70)
triangle1.__next__()
triangle1.__next__()
triangle1.__next__()

print('*'*70)
triangle1.sides()
