from PublicTransport import PublicTransport


class Tram(PublicTransport):  # класс tram наследуется от PublicTransport
    def __init__(self, id, name, capacity, speed, route_number):
        super().__init__(id, name, capacity, speed)
        self._passengers = 0
        self._route_number = route_number
        self._current_stop = None

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict.update({
            "type": "Tram",
            "route_number": self._route_number,
            "passengers": self._passengers,
            "current_stop": self._current_stop
        })
        return base_dict

    @classmethod
    def from_dict(cls, data):
        tram = cls(
            id=data["id"],
            name=data["name"],
            capacity=data["capacity"],
            speed=data["speed"],
            route_number=data["route_number"]
        )
        tram._passengers = data["passengers"]
        tram._current_stop = data["current_stop"]
        return tram

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

