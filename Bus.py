from PublicTransport import PublicTransport


class Bus(PublicTransport):  # класс Bus наследуется от Public_Transport

    def __init__(self, id, name, capacity, speed, route_number):  # значение по умолчанию
        super().__init__(id, name, capacity, speed)
        self._passengers = 0
        self._route_number = route_number
        self._current_stop = None

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict.update({
            "type": "Bus",
            "route_number": self._route_number,
            "passengers": self._passengers,
            "current_stop": self._current_stop
        })
        return base_dict

    @classmethod
    def from_dict(cls, data):
        bus = cls(
            id=data["id"],
            name=data["name"],
            capacity=data["capacity"],
            speed=data["speed"],
            route_number=data["route_number"]
        )
        bus._passengers = data["passengers"]
        bus._current_stop = data["current_stop"]
        return bus

    def set_capacity(self):
        try:
            self._capacity = int(input("вместимость драндулета: "))
            while self._capacity >= 100 or self._capacity <= 10:
                print("куда столько. подумай еще")
                self._capacity = int(input("спрашиваю в последний раз. вместимость драндулета: "))
        except ValueError:
            print("введи числа, а не буквы")

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
        if self._speed > 0 and distance > 0:
            time = distance / self._speed
            print(f"Время до следующей остановки: {time:.2f} часов.")
            return time
        else:
            print("Скорость автобуса и его вместимость должны быть положительными для расчета времени.")
            return None

