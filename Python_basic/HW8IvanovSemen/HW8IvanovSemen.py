# Создайте класс "животное". Наполните его данными и методами на свое усмотрение. Пропишите в методах
# класса докстринги с описанием метода

class Animal:
    height = ''
    weight = ''
    legsQuantity = 4

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight


class Cat(Animal):
    name = 'Aiisa'
    color = 'tiger red'
    age = 1.5
    foodType = 'meat, milk'

    def noiseAtNight(self):
        """----кошачий ночной тыгыдык----"""
        print('Вставайте, я вам спать не дам')

    def runQuickly(self):
        """----умею быстро бегать----"""
        print('Ok, let\'s go !!!')

    def makingNoise(self):
        """----могу мурчать и мяукать----"""
        print('meowww')

    def foodTime(self, food):
        """----Покорми меня----"""
        print(f'It\'s time to take some food {food}')


cat1 = Cat(40, 2.5)
print(cat1.name)
print(f'Cat\'s height ----> {cat1.height} cm')
print(f'Cat\'s weight ----> {cat1.weight} kg')
print(f'Cat\'s age ----> {cat1.age} years')

print(cat1.makingNoise.__doc__)
cat1.makingNoise()

print(cat1.runQuickly.__doc__)
cat1.runQuickly()

print(cat1.noiseAtNight.__doc__)
cat1.noiseAtNight()

print(cat1.foodTime.__doc__)
cat1.foodTime(cat1.foodType)

print('-'*50)

# 3* Задание. Сделать второе задание в питоне.

# Из своей диаграммы второго задания я описал ветку наземного транспорта.


class Vehicles:
    productYear = 2000
    numberOfPassengers = 4
    numberOfDrivers = 2

    def moveFromAtoB(self):
        print('Prepare. Begin to move....')


class EarthVehicles(Vehicles):
    numberOfWheels = 8
    massOfVehicle = 3000
    maxSpeed = 200


class RoadVehicles(EarthVehicles):
    mark = 'some mark'
    model = 'some model'
    sizeOfTyres = 'size of tyres...'

    def __init__(self, mrk, mod, tyreSize):
        print(f'Initializing road-vehicle : {mrk}, {mod}, {tyreSize}')
        self.mark = mrk
        self.model = mod
        self.sizeOfTyres = tyreSize

    def tyresAutoPump(self, tyresSize):

        """This is Tyres Auto-Pump System of your Vehicle.
        It checks the pressure inside your wheels,
        and begins to pump it automatically"""

        if not isinstance(tyresSize, (int, float)):
            raise TypeError('Wrong type tyres size')
        print(f'Your tyres size is {tyresSize}. Auto-pump process begins...')


class Automobile(RoadVehicles):
    airConditioner = 'yes or no'

    def climateControl(self, airCond):
        if self.airConditioner.lower() == 'yes':
            print('Turn climate on/off')
        elif self.airConditioner.lower() == 'no':
            print('There is no Climate control in this model')
        else:
            print('Unknown command')


car1 = Automobile('Mazda', '3', 195)
car1.numberOfPassengers = 3
car1.numberOfDrivers = 1
car1.numberOfWheels = 4
car1.productYear = 2010
car1.massOfVehicle = 1550
car1.maxSpeed = 240
car1.airConditioner = 'no'

print(f'Number of wheels: {car1.numberOfWheels}')
print(f'Number of passengers: {car1.numberOfPassengers}')
print(f'Climate control: {car1.airConditioner}')
print(f'Mass of car: {car1.massOfVehicle}kg')
print(f'Max speed of car: {car1.maxSpeed}km/h')
car1.climateControl(car1.airConditioner)
car1.tyresAutoPump(car1.sizeOfTyres)
car1.moveFromAtoB()

print('-'*50)


class Motocycle(RoadVehicles):
    antiTheftSystem = 'yes or no'

    def wheelsBlockSystem(self, antiTheft):

        """This is Anti-Theft System of your moto. It blocks your wheels when the engine is off.
        You need to unblock it before riding your bike"""

        if self.antiTheftSystem.lower() == 'yes':
            print('Wheels are blocked! You need to turn off your moto anti-theft system before ride')
        elif self.antiTheftSystem.lower() == 'no':
            print('There is no anti-theft system on this model of moto')
        else:
            print('Unknown command')


moto1 = Motocycle('Yamaha', 'r1', 190)
moto1.numberOfDrivers = 1
moto1.numberOfPassengers = 1
moto1.numberOfWheels = 2
moto1.productYear = 2013
moto1.massOfVehicle = 206
moto1.maxSpeed = 315
moto1.antiTheftSystem = 'yes'

print(f'Number of wheels: {car1.numberOfWheels}')
print(f'Number of passengers: {car1.numberOfPassengers}')
print(f'Mass of moto: {moto1.massOfVehicle}kg')
print(f'Max speed of moto: {moto1.maxSpeed}km/h')
moto1.wheelsBlockSystem(moto1.antiTheftSystem)
moto1.tyresAutoPump(moto1.sizeOfTyres)
moto1.moveFromAtoB()
