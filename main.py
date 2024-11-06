"""
1) ̶Н̶у̶ж̶н̶о̶ ̶д̶о̶б̶а̶в̶и̶т̶ь̶ ̶п̶р̶о̶в̶е̶р̶к̶у̶ ̶н̶а̶ ̶и̶м̶я̶,̶ ̶ч̶т̶о̶б̶ы̶ ̶в̶ы̶з̶ы̶в̶а̶т̶ь̶ ̶к̶о̶н̶с̶т̶р̶у̶к̶т̶о̶р̶ ̶т̶о̶г̶о̶ ̶и̶л̶и̶ ̶и̶н̶о̶г̶о̶ ̶к̶л̶а̶с̶с̶а̶ ̶в̶ ̶C̶R̶U̶D̶
2) ̶Д̶о̶б̶а̶в̶и̶т̶ь̶ ̶а̶н̶а̶л̶о̶г̶ ̶s̶t̶a̶t̶i̶c̶_̶c̶a̶s̶t̶ ̶п̶е̶р̶е̶м̶е̶н̶н̶о̶й̶,̶ ̶ч̶т̶о̶б̶ы̶ ̶к̶а̶ж̶д̶ы̶й̶ ̶о̶б̶ъ̶е̶к̶т̶ ̶л̶ю̶б̶о̶г̶о̶ ̶д̶о̶ч̶е̶р̶н̶е̶г̶о̶ ̶к̶л̶а̶с̶с̶а̶ ̶и̶м̶е̶л̶ ̶с̶о̶б̶с̶т̶в̶е̶н̶н̶ы̶й̶ ̶i̶d̶
3) ̶Д̶о̶д̶е̶л̶а̶т̶ь̶ ̶м̶е̶т̶о̶д̶ы̶ ̶C̶R̶U̶D̶
4)Добавить еще несколько классов транспорта
5)XML, Json
"""


class Public_Transport:
    def __init__(self,id, name, capacity, speed):  # значение по умолчанию
        self._id = id
        self._name = name
        self._capacity = capacity
        self._speed = speed


    def __repr__(self):
        # __str__ - специальный метод строкового представления объекта
        return f"Transport(id = {self._id}, name = '{self._name}', capacity = {self._capacity}, speed = {self._speed})"


class Bus(Public_Transport): #класс Bus наследуется от Public_Transport

    def __init__(self, id ,name, capacity, speed): #значение по умолчанию
        Public_Transport.__init__(self, id, name, capacity, speed)

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
    def __init__(self, id, name, capacity, speed):
        self._id = id
        self._name = name
        self._capacity = capacity
        self._speed = speed


    def get_info(self):
        print(self)
        print("Название объекта:", self._name)


class TransportManager:
    """Класс для управления CRUD-операциями с объектами Transport"""

    def __init__(self):
        self.transport_list = []
        self.current_id = 1

    def create(self, name, capacity, speed):
        """Создает и добавляет новый транспорт в список"""
        if name == "Bus":
            transport = Bus(self.current_id, name, capacity, speed)
            self.transport_list.append(transport)
            self.current_id+=1
            return transport
        elif name == "Tram":
            transport = Tram(self.current_id, name, capacity, speed)
            self.transport_list.append(transport)
            self.current_id += 1
            return transport


    def read_all(self):
        """Возвращает список всего транспорта"""
        return self.transport_list

    def read_by_id(self, current_id):
        """Возвращает транспорт по его ID"""
        for transport in self.transport_list:
            if transport._id == current_id:
                return transport
        return None


    def update(self, current_id, name=None, capacity=None, speed=None):
        """Обновляет данные о транспорте по его ID"""
        transport = self.read_by_id(current_id)
        if transport:
            if name is not None:
                transport._name = name
            if capacity is not None:
                transport._capacity = capacity
            if speed is not None:
                transport._speed = speed
            return transport
        return None

    def delete(self, current_id):
       """Удаляет транспорт по его ID"""
       transport = self.read_by_id(current_id)
       if transport:
            self.transport_list.remove(transport)
            for transport in self.transport_list:
                transport._id-=1
            return f"Transport with id {current_id} has been deleted."

       return "Person not found."


manager = TransportManager()

# Create
print("Create")
transport1 = manager.create("Bus", 15, 70)
transport2 = manager.create("Bus", 60, 40)
transport3 = manager.create("Tram", 50, 30)
print(transport1, transport2, transport3)

# Read all
print("Read all")
all_transport = manager.read_all()
print(all_transport)

# Read by ID
print("Read by id")
manager.read_by_id(1)


# Update
updated_transport = manager.update(1, name="Tram", capacity=78, speed=30)
print("Updated transport (1):", updated_transport)

# Delete
delete_message = manager.delete(2)
print(delete_message)

print("All transport after deletion:", manager.read_all())