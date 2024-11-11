"""
1) ̶Н̶у̶ж̶н̶о̶ ̶д̶о̶б̶а̶в̶и̶т̶ь̶ ̶п̶р̶о̶в̶е̶р̶к̶у̶ ̶н̶а̶ ̶и̶м̶я̶,̶ ̶ч̶т̶о̶б̶ы̶ ̶
в̶ы̶з̶ы̶в̶а̶т̶ь̶ ̶к̶о̶н̶с̶т̶р̶у̶к̶т̶о̶р̶ ̶т̶о̶г̶о̶ ̶и̶л̶и̶ ̶и̶н̶о̶г̶о̶ ̶к̶л̶а̶с̶с̶а̶ ̶в̶ ̶C̶R̶U̶D̶
2) ̶Д̶о̶б̶а̶в̶и̶т̶ь̶ ̶а̶н̶а̶л̶о̶г̶ ̶s̶t̶a̶t̶i̶c̶_̶c̶a̶s̶t̶ ̶п̶е̶р̶е̶м̶е̶н̶н̶о̶й̶,̶ ̶
ч̶т̶о̶б̶ы̶ ̶к̶а̶ж̶д̶ы̶й̶ ̶о̶б̶ъ̶е̶к̶т̶ ̶
л̶ю̶б̶о̶г̶о̶ ̶д̶о̶ч̶е̶р̶н̶е̶г̶о̶ ̶к̶л̶а̶с̶с̶а̶ ̶и̶м̶е̶л̶ ̶с̶о̶б̶с̶т̶в̶е̶н̶н̶ы̶й̶ ̶i̶d̶
3) ̶Д̶о̶д̶е̶л̶а̶т̶ь̶ ̶м̶е̶т̶о̶д̶ы̶ ̶C̶R̶U̶D̶
4) ̶Д̶о̶б̶а̶в̶и̶т̶ь̶ ̶е̶щ̶е̶ ̶н̶е̶с̶к̶о̶л̶ь̶к̶о̶ ̶к̶л̶а̶с̶с̶о̶в̶ ̶т̶р̶а̶н̶с̶п̶о̶р̶т̶а̶
5)XML,  ̶J̶s̶o̶n̶
6)удалить эти комментарии
"""

from CRUD import TransportManager
import database

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

# Json
transport_list = [bus, tram, metro]

# Сохраняем в файл
database.save_to_json("transport_data.json", transport_list)

# Загружаем из файла
loaded_transport = database.load_from_json("transport_data.json")

# Проверяем, что данные загружены корректно
for transport in loaded_transport:
    print(transport.to_dict())
