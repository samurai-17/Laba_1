
class Public_Transport:
    def __init__(self, name='Transport', capacity = 0, max_speed = 0):  # значение по умолчанию
        self._name = name
        self._capacity = capacity
        self._max_speed = max_speed


    def __str__(self):
        # __str__ - специальный метод строкового представления объекта
        return f'{self._name} object'

class Bus(Public_Transport): #класс Bus наследуется от Public_Transport

    def __init__(self, name = 'Bus', capacity = 1, max_speed = 50): #значение по умолчанию
        Public_Transport.__init__(self, name, capacity, max_speed)

    def __str__(self):
        # __str__ - специальный метод строкового представления объекта
        return f'Меня зовут {self._name} и я автобус'

    def set_capacity(self):
        try:
            self._capacity = int(input("вместимость драндулета: "))
            while (self._capacity >= 100 or self._capacity <= 10):
                print("куда столько. подумай еще")
                self._capacity = int(input("спрашиваю в последний раз. вместимость драндулета: "))
        except ValueError:
            print("введи числа, а не буквы")


    def get_capacity(self):
        return self._capacity

    def max_speed(self):
        if self._capacity < 50:
            print("максимальная скорость равна",50)
        elif 100 > self._capacity > 50:
            print("максимальная скорость равна", 35)

class tram(Public_Transport): #класс Bus наследуется от Public_Transport
    def __init__(self, name, number):
        self._name = name
        self._number = number



t = Bus("Галина", 40)
print(t)
print(t.get_capacity())
t.set_capacity()
print("вместимость = ", t.get_capacity())
t.max_speed()
