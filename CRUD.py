from Bus import Bus
from Tram import Tram
from metro import Metro


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

    def update(self, current_id, capacity=None, speed=None):
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
