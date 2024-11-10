"""
1) ̶Н̶у̶ж̶н̶о̶ ̶д̶о̶б̶а̶в̶и̶т̶ь̶ ̶п̶р̶о̶в̶е̶р̶к̶у̶ ̶н̶а̶ ̶и̶м̶я̶,̶ ̶ч̶т̶о̶б̶ы̶ ̶
в̶ы̶з̶ы̶в̶а̶т̶ь̶ ̶к̶о̶н̶с̶т̶р̶у̶к̶т̶о̶р̶ ̶т̶о̶г̶о̶ ̶и̶л̶и̶ ̶и̶н̶о̶г̶о̶ ̶к̶л̶а̶с̶с̶а̶ ̶в̶ ̶C̶R̶U̶D̶
2) ̶Д̶о̶б̶а̶в̶и̶т̶ь̶ ̶а̶н̶а̶л̶о̶г̶ ̶s̶t̶a̶t̶i̶c̶_̶c̶a̶s̶t̶ ̶п̶е̶р̶е̶м̶е̶н̶н̶о̶й̶,̶ ̶
ч̶т̶о̶б̶ы̶ ̶к̶а̶ж̶д̶ы̶й̶ ̶о̶б̶ъ̶е̶к̶т̶ ̶
л̶ю̶б̶о̶г̶о̶ ̶д̶о̶ч̶е̶р̶н̶е̶г̶о̶ ̶к̶л̶а̶с̶с̶а̶ ̶и̶м̶е̶л̶ ̶с̶о̶б̶с̶т̶в̶е̶н̶н̶ы̶й̶ ̶i̶d̶
3) ̶Д̶о̶д̶е̶л̶а̶т̶ь̶ ̶м̶е̶т̶о̶д̶ы̶ ̶C̶R̶U̶D̶
4) ̶Д̶о̶б̶а̶в̶и̶т̶ь̶ ̶е̶щ̶е̶ ̶н̶е̶с̶к̶о̶л̶ь̶к̶о̶ ̶к̶л̶а̶с̶с̶о̶в̶ ̶т̶р̶а̶н̶с̶п̶о̶р̶т̶а̶
5)XML, Json
6)удалить эти комментарии
"""


class PublicTransport:
    def __init__(self, id, name, capacity, speed):  # значение по умолчанию
        self._id = id
        self._name = name
        self._capacity = capacity
        self._speed = speed
        self._in_motion = False


    def __repr__(self):
        # __str__ - специальный метод строкового представления объекта
        return f"Transport(id = {self._id}, name = '{self._name}', capacity = {self._capacity}, speed = {self._speed})"


class Bus(PublicTransport):  # класс Bus наследуется от Public_Transport

    def __init__(self, id, name, capacity, speed, route_number):  # значение по умолчанию
        PublicTransport.__init__(self, id, name, capacity, speed)
        self._passengers = 0
        self._route_number = route_number
        self._current_stop = None

    def start(self):
        """Запуск движения автобуса."""
        if not self._in_motion:
            self._in_motion = True
            print(f"Автобус на маршруте {self._route_number} начал движение.")
        else:
            print("Автобус уже в движении.")

    def stop(self):
        """Остановка автобуса на текущей остановке."""
        if self._in_motion:
            self._in_motion = False
            print(f"Автобус на маршруте {self._route_number} остановился.")
        else:
            print("Автобус уже остановлен.")

    def arrive_at_stop(self, stop_name):
        """Прибытие автобуса на остановку."""
        self.stop()  # Останавливаем трамвай на остановке
        self._current_stop = stop_name
        self._in_motion = False
        print(f"Автобус на маршруте {self._route_number} прибыл на остановку '{stop_name}'.")

    def depart_from_stop(self):
        """Отправление автобуса от остановки."""
        self.start()  # Запускаем движение трамвая
        print(f"Автобус на маршруте {self._route_number} отправился от остановки '{self._current_stop}'.")
        self._current_stop = None  # Трамвай покинул остановку
        self._in_motion = True

    def board_passengers(self, count):
        """Посадка пассажиров в автобус."""
        if self._in_motion:
            print("Посадка невозможна! Автобус в движении.")
        else:
            if self._passengers + count <= self._capacity:
                self._passengers += count
                print(f"{count} пассажиров сели в автобус. Всего пассажиров: {self._passengers}.")
            else:
                available_space = self._capacity - self._passengers
                print(f"Автобус переполнен! Могут сесть только {available_space} пассажиров.")
                self._passengers += available_space

    def alight_passengers(self, count):
        """Высадка пассажиров из автобуса."""
        if self._in_motion:
            print("Высадка невозможна! Автобус в движении.")
        else:
            if count <= self._passengers:
                self._passengers -= count
                print(f"{count} пассажиров вышли из автобуса. Осталось пассажиров: {self._passengers}.")
            else:
                print(f"В автобусе всего {self._passengers} пассажиров, высадка всех.")
                self._passengers = 0

    def calculate_time_to_next_stop(self, distance):
        """Рассчитать время до следующей остановки на основе скорости и расстояния."""
        if self._speed > 0:
            time = distance / self._speed
            print(f"Время до следующей остановки: {time:.2f} часов.")
            return time
        else:
            print("Скорость автобуса должна быть положительной для расчета времени.")
            return None


class Tram(PublicTransport):  # класс tram наследуется от PublicTransport
    def __init__(self, id, name, capacity, speed, route_number):
        super().__init__(id, name, capacity, speed)
        self._passengers = 0
        self._route_number = route_number
        self._current_stop = None

    def start(self):
        """Запуск движения трамвая."""
        if not self._in_motion:
            self._in_motion = True
            print(f"Трамвай на маршруте {self._route_number} начал движение.")
        else:
            print("Трамвай уже в движении.")

    def stop(self):
        """Остановка трамвая на текущей остановке."""
        if self._in_motion:
            self._in_motion = False
            print(f"Трамвай на маршруте {self._route_number} остановился.")
        else:
            print("Трамвай уже остановлен.")

    def arrive_at_stop(self, stop_name):
        """Прибытие трамвая на остановку."""
        self.stop()  # Останавливаем трамвай на остановке
        self._current_stop = stop_name
        self._in_motion = False
        print(f"Трамвай на маршруте {self._route_number} прибыл на остановку '{stop_name}'.")

    def depart_from_stop(self):
        """Отправление трамвая от остановки."""
        self.start()  # Запускаем движение трамвая
        print(f"Трамвай на маршруте {self._route_number} отправился от остановки '{self._current_stop}'.")
        self._current_stop = None  # Трамвай покинул остановку
        self._in_motion = True

    def board_passengers(self, count):
        """Посадка пассажиров в трамвай."""
        if self._in_motion:
            print("Посадка невозможна! Трамвай в движении.")
        else:
            if self._passengers + count <= self._capacity:
                self._passengers += count
                print(f"{count} пассажиров сели в трамвай. Всего пассажиров: {self._passengers}.")
            else:
                available_space = self._capacity - self._passengers
                print(f"Трамвай переполнен! Могут сесть только {available_space} пассажиров.")
                self._passengers += available_space

    def alight_passengers(self, count):
        """Высадка пассажиров из трамвая."""
        if self._in_motion:
            print("Высадка невозможна! Трамвай в движении.")
        else:
            if count <= self._passengers:
                self._passengers -= count
                print(f"{count} пассажиров вышли из трамвая. Осталось пассажиров: {self._passengers}.")
            else:
                print(f"В трамвае всего {self._passengers} пассажиров, высадка всех.")
                self._passengers = 0


class Metro(PublicTransport):  # класс Metro наследуется от PublicTransport
    def __init__(self, id, name, capacity, speed, line_name, stations, interval):
        super().__init__(id, name, capacity, speed)
        self._line_name = line_name
        self._stations = stations
        self._interval = interval
        self._direction = 1
        self._current_station = stations[0]
        self._passengers = 0

    def start(self):
        """Начать движение метро."""
        if not self._in_motion:
            self._in_motion = True
            if self._current_station == "Депо":
                print(f"Поезд линии {self._line_name} отправляется из '{self._current_station}'.")
            else:
                print(f"Поезд линии {self._line_name} отправляется со станции '{self._current_station}'.")
        else:
            print("Поезд уже в движении.")

    def stop(self):
        """Остановить поезд на текущей станции."""
        if self._in_motion:
            self._in_motion = False
            if self._current_station == "Депо":
                print(f"Поезд линии {self._line_name} вернулся в '{self._current_station}'.")
            else:
                print(f"Поезд линии {self._line_name} остановился на станции '{self._current_station}'.")
        else:
            print("Поезд уже остановлен.")

    def arrive_at_next_station(self):
        """Переместить поезд на следующую станцию."""
        if self._in_motion:
            current_index = self._stations.index(self._current_station)
            next_index = current_index + self._direction

            # Проверка на конец линии для смены направления
            if next_index < 0 or next_index >= len(self._stations):
                self._direction *= -1
                next_index = current_index + self._direction

            self._current_station = self._stations[next_index]
            self.stop()  # Остановимся на следующей станции
        else:
            print("Поезд должен начать движение для прибытия на следующую станцию.")

    def board_passengers(self, count):
        """Посадка пассажиров с учетом вместимости состава."""
        if self._passengers + count <= self._capacity:
            self._passengers += count
            print(f"{count} пассажиров сели в поезд. Всего пассажиров: {self._passengers}.")
        else:
            available_space = self._capacity - self._passengers
            self._passengers += available_space
            print(f"Поезд переполнен! Могут сесть только {available_space} пассажиров.")

    def alight_passengers(self, count):
        """Высадка пассажиров из поезда."""
        if count <= self._passengers:
            self._passengers -= count
            print(f"{count} пассажиров вышли из поезда. Осталось пассажиров: {self._passengers}.")
        else:
            print(f"В поезде всего {self._passengers} пассажиров, высаживаем всех.")
            self._passengers = 0

    def calculate_time_to_next_station(self, distance):
        """Рассчитать время до следующей станции по скорости и расстоянию."""
        if self._speed > 0:
            time = distance / self._speed
            print(f"Время до следующей станции: {time:.2f} часов.")
            return time
        else:
            print("Скорость должна быть положительной для расчета времени.")
            return None


class TransportManager:
    """Класс для управления CRUD-операциями с объектами Transport"""

    def __init__(self):
        self.transport_list = []
        self.current_id = 1

    def create(self, name, capacity, speed, route_number=None, line_name=None, stations=None, interval=None):
        """Создает и добавляет новый транспорт в список"""
        if name == "Bus":
            transport = Bus(self.current_id, name, capacity, speed, route_number)
            self.transport_list.append(transport)
            self.current_id += 1
            return transport
        elif name == "Tram":
            transport = Tram(self.current_id, name, capacity, speed, route_number)
            self.transport_list.append(transport)
            self.current_id += 1
            return transport
        elif name == "Metro":
            transport = Metro(self.current_id, name, capacity, speed, line_name, stations, interval)
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

    def update(self, current_id,capacity=None, speed=None):
        """Обновляет данные о транспорте по его ID"""
        transport = self.read_by_id(current_id)
        if transport:
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
            return f"Transport with id {current_id} has been deleted."
        return "Transport not found."


manager = TransportManager()

# Create
print("Create")
bus = manager.create("Bus", 50, 35, 13)
tram = manager.create("Tram", 50, 40, 5)
metro = manager.create(name="Metro", capacity=200, speed=70, line_name="Кольцевая",
                       stations=["Депо", "Станция А", "Станция Б", "Станция В"], interval=10)
print(bus, tram, metro)

# Read all
print("Read all")
all_transport = manager.read_all()
print(all_transport)

# Read by ID
print("Read by id")
manager.read_by_id(1)

# Update
updated_transport = manager.update(1, capacity=78, speed=30)
print("Updated transport (1):", updated_transport)

# Delete
delete_transport = manager.delete(2)
print(delete_transport)

print("All transport after deletion:", manager.read_all())
# Создаем автобус на маршруте 10, вместимостью 50 человек, с ценой билета 30 рублей и скоростью 40 км/ч

print("-----------------------")
# Начинаем движение, прибываем на остановку, посадка и высадка пассажиров
bus.start()
bus.arrive_at_stop("Площадь Ленина")
bus.board_passengers(30)
bus.alight_passengers(10)
bus.depart_from_stop()

# Рассчитываем время до следующей остановки (например, расстояние 15 км)
bus.calculate_time_to_next_stop(distance=15)

print("-----------------------")



# Начало движения, прибытие на остановку, посадка и высадка пассажиров
tram.start()
tram.arrive_at_stop("Центральная площадь")
tram.board_passengers(50)
tram.alight_passengers(20)
tram.depart_from_stop()
print("-----------------------")



# Начинаем движение, прибываем на следующую станцию, посадка и высадка пассажиров
metro.start()
metro.arrive_at_next_station()

metro.board_passengers(150)
metro.start()
metro.arrive_at_next_station()
metro.alight_passengers(50)

# Рассчитываем время до следующей станции (например, расстояние 5 км)
metro.calculate_time_to_next_station(distance=5)

