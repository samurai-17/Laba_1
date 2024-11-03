"""
1)Нужно добавить проверку на имя, чтобы вызывать конструтор того или иного класса в CRUD
2)Добавить аналог static_cast переменной, чтобы каждый объект любого дочернего класса имел собственный id
3)Добавить еще несколько классов транспорта
4)XML, Json
"""


class Public_Transport:
    def __init__(self, id, name, capacity, speed):  # значение по умолчанию
        self._id = id
        self._name = name
        self._capacity = capacity
        self._speed = speed


    def __repr__(self):
        # __str__ - специальный метод строкового представления объекта
        return f"Transport(id = {self._id}, name = '{self._name}', capacity = {self._capacity}, speed = {self._speed})"


class Bus(Public_Transport): #класс Bus наследуется от Public_Transport

    def __init__(self, name, capacity, speed): #значение по умолчанию
        Public_Transport.__init__(self, name, capacity, speed)

    def __str__(self):
        # __str__ - специальный метод строкового представления объекта
        return f'Это автобус. Его вместимость = {self._capacity}, а скорость равна {self._speed}'

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
            print("максимальная скорость равна", 50)
        elif 100 > self._capacity > 50:
            print("максимальная скорость равна", 35)

class Tram(Public_Transport): #класс tram наследуется от Public_Transport
    def __init__(self, name, capacity, speed, number):
        self._name = name
        self._capacity = capacity
        self._speed = speed
        self._number = number

    def get_info(self):
        print(self)
        print("Название объекта:", self._name)
        print("Трамвай номер:", self._number)

class TransportManager:
    """Класс для управления CRUD-операциями с объектами Transport"""

    def __init__(self):
        self.transport_list = []

    def create(self, name, capacity, speed):
        """Создает и добавляет нового человека в список"""
        transport = Public_Transport(name, capacity, speed)
        self.transport_list.append(transport)
        return transport

    def read_all(self):
        """Возвращает список всех людей"""
        return self.transport_list

    def read_by_id(self, name):
        """Возвращает человека по его ID"""
        unique_count = 0
        for transport in self.transport_list:
            if transport._name == name:
                unique_count += 1
                print("Найденный объект номер", unique_count)
                print("Наименование:", transport._name, "Вместимость:", transport._capacity, "Скорость:", transport._speed)
        return None

    """
    def update(self, person_id, name=None, age=None):
        Обновляет данные о человеке по его ID
        transport = self.read_by_id(person_id)
        if person:
            if name is not None:
                person.name = name
            if age is not None:
                person.age = age
            return person
        return None

    def delete(self, person_id):
       Удаляет человека по его ID
        person = self.read_by_id(person_id)
        if person:
            self.people_list.remove(person)
            return f"Person with id {person_id} has been deleted."
        return "Person not found."
"""

manager = TransportManager()
transport1 = manager.create("Bus", 15, 70)
transport2 = manager.create("Bus", 60, 40)
print(transport1, transport2)
all_transport = manager.read_all()
print(all_transport)
manager.read_by_id("Bus")

