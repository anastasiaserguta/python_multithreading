from threading import Thread
from time import sleep
from random import randint

# Словарь имен потоков и их миссий
# Полный словарь вшит в задачу
missions = {
    "Thread-Scan": "Сканирование данных",
    "Thread-Hack": "Взлом системы",
}

# Описание задачи для потоков
def mission(mission_name):
    print(f'[{mission_name}] Миссия началась.')
    sleep(randint(1, 3))
    print(f"[{mission_name}] Миссия успешно выполнена!")


def main():
    for k in missions.keys():
        thread = Thread(target=mission, name=k, args=(missions[k],))
        print(f"[{thread.name} ({missions[k]})] Статус миссии до запуска: {thread.is_alive()}")
        thread.start()
        print(f"[{thread.name} ({missions[k]})] Миссия активна: {thread.is_alive()}")
        thread.join()
        print(f"[{thread.name} ({missions[thread.name]})] Статус миссии после завершения: {not thread.is_alive()}")

main()