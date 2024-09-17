from threading import Thread, Timer, active_count
from time import sleep
# Словарь с моделями самолетов и временем полета      

aircrafts = {
    'Boeing 737': 6, 
    'Airbus A320': 9, 
    'Boeing 747': 6, 
    'Airbus A380': 7,
}

# Функция для печати сообщений о начале и завершении полета.
def flight_simulation(model, flight_time):
    print(f"{model} начал полет. Время полета: {flight_time} сек.")
    sleep(int(flight_time))
    print(f"{model} завершил полет.")


def main():
    for air in aircrafts.keys():
        thread = Thread(target=flight_simulation, args=(air, aircrafts[air]))
        thread.start()

def active():
    print(f"Количество самолетов в воздухе после 5 секунд: {active_count() - 2}")

timer = Timer(5, active)
timer.start()
main()

