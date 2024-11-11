import xml.etree.ElementTree as ET


class PublicTransport:
    def __init__(self, id, name, capacity, speed):  # значение по умолчанию
        self._id = id
        self._name = name
        while capacity == str(capacity):
            print("введи число, а не буквы")
            print("capacity: ")
            try:
                capacity = int(input())
            except ValueError:
                print("в следующий раз вводи число")
        self._capacity = capacity
        while speed == str(speed):
            print("введи число, а не буквы")
            print("speed: ")
            try:
                speed = int(input())
            except ValueError:
                print("в следующий раз вводи число")
        self._speed = speed
        self._in_motion = False

    def to_dict(self):
        return {
            "type": "PublicTransport",
            "id": self._id,
            "name": self._name,
            "capacity": self._capacity,
            "speed": self._speed,
            "in_motion": self._in_motion
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            name=data["name"],
            capacity=data["capacity"],
            speed=data["speed"]
        )

    def to_xml(self):
        element = ET.Element("PublicTransport")
        ET.SubElement(element, "id").text = str(self._id)
        ET.SubElement(element, "name").text = self._name
        ET.SubElement(element, "capacity").text = str(self._capacity)
        ET.SubElement(element, "speed").text = str(self._speed)
        ET.SubElement(element, "in_motion").text = str(self._in_motion)
        return element

    @classmethod
    def from_xml(cls, element):
        return cls(
            id=int(element.find("id").text),
            name=element.find("name").text,
            capacity=int(element.find("capacity").text),
            speed=int(element.find("speed").text)
        )

    def __repr__(self):
        # __str__ - специальный метод строкового представления объекта
        return f"Transport(id = {self._id}, name = '{self._name}', capacity = {self._capacity}, speed = {self._speed})"
