from PublicTransport import *


class Metro(PublicTransport):  # класс Metro наследуется от PublicTransport
    def __init__(self, id, name, capacity, speed, line_name, stations, interval):
        super().__init__(id, name, capacity, speed)
        self._line_name = line_name
        self._stations = stations
        self._interval = interval
        self._direction = 1
        self._current_station = stations[0]
        self._passengers = 0

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict.update({
            "type": "Metro",
            "line_name": self._line_name,
            "stations": self._stations,
            "interval": self._interval,
            "current_station": self._current_station,
            "passengers": self._passengers,
            "direction": self._direction
        })
        return base_dict

    @classmethod
    def from_dict(cls, data):
        metro = cls(
            id=data["id"],
            name=data["name"],
            capacity=data["capacity"],
            speed=data["speed"],
            line_name=data["line_name"],
            stations=data["stations"],
            interval=data["interval"]
        )
        metro._current_station = data["current_station"]
        metro._passengers = data["passengers"]
        metro._direction = data["direction"]
        return metro

    def to_xml(self):
        element = super().to_xml()
        element.tag = "Metro"
        ET.SubElement(element, "line_name").text = self._line_name
        stations_element = ET.SubElement(element, "stations")
        for station in self._stations:
            ET.SubElement(stations_element, "station").text = station
        ET.SubElement(element, "interval").text = str(self._interval)
        ET.SubElement(element, "current_station").text = self._current_station
        ET.SubElement(element, "passengers").text = str(self._passengers)
        ET.SubElement(element, "direction").text = str(self._direction)
        return element

    @classmethod
    def from_xml(cls, element):
        stations = [station.text for station in element.find("stations").findall("station")]
        metro = cls(
            id=int(element.find("id").text),
            name=element.find("name").text,
            capacity=int(element.find("capacity").text),
            speed=int(element.find("speed").text),
            line_name=element.find("line_name").text,
            stations=stations,
            interval=int(element.find("interval").text)
        )
        metro._current_station = element.find("current_station").text
        metro._passengers = int(element.find("passengers").text)
        metro._direction = int(element.find("direction").text)
        return metro

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
        if self._speed > 0 and distance > 0:
            time = distance / self._speed
            print(f"Время до следующей станции: {time:.2f} часов.")
            return time
        else:
            print("Скорость и дистанция должны быть положительными для расчета времени.")
            return None
