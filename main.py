from CRUD import TransportManager
import database
from database_xml import *

manager = TransportManager()

# Create
print("Create")
bus = manager.create("Bus", 30, 35, 13)

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

print("------------------------------------")
# Начинаем движение, прибываем на остановку, посадка и высадка пассажиров
bus.start()
bus.arrive_at_stop("Площадь Ленина")
bus.board_passengers(30)
bus.alight_passengers(10)
bus.depart_from_stop()

# Рассчитываем время до следующей остановки (например, расстояние 15 км)
bus.calculate_time_to_next_stop(distance=15)

print("------------------------------------")

# Начало движения, прибытие на остановку, посадка и высадка пассажиров
tram.start()
tram.arrive_at_stop("Центральная площадь")
tram.board_passengers(50)
tram.alight_passengers(20)
tram.depart_from_stop()
print("------------------------------------")

# Начинаем движение, прибываем на следующую станцию, посадка и высадка пассажиров
metro.start()
metro.arrive_at_next_station()
metro.board_passengers(150)
metro.start()
metro.arrive_at_next_station()
metro.alight_passengers(50)

# Рассчитываем время до следующей станции (например, расстояние 5 км)
metro.calculate_time_to_next_station(distance=5)
print("------------------------------------")
# Json
transport_list = [bus, tram, metro]

# Сохраняем в файл
database.save_to_json("transport_data.json", transport_list)

# Загружаем из файла
loaded_transport = database.load_from_json("transport_data.json")

# Проверяем, что данные загружены корректно
print("Json")
for transport in loaded_transport:
    print(transport.to_dict())
print("------------------------------------")

# Сохраняем в XML-файл
save_to_xml("transport_data.xml", transport_list)

# Загружаем из XML-файла
loaded_transport = load_from_xml("transport_data.xml")

# Проверяем, что данные загружены корректно
print("XML")
for transport in loaded_transport:
    print(ET.tostring(transport.to_xml(), encoding="utf-8").decode("utf-8"))
print("------------------------------------")
