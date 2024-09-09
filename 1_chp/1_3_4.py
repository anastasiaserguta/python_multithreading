from threading import Thread

# Глобальные переменные для массивов
array_descending = [733, 725, 389, 606, 544, 526, 496, 448, 345, 239]
array_ascending = [124, 168, 350, 501, 389, 419, 428, 662, 760, 829]
symbols_array = ['g', 'e', 'k', 'a', 'w', 'z', 'o', 'b', 'm', 'l', 'h', 'n', 'd', 's', 'q']


# Создайте и запустите потоки для сортировки
thread1 = Thread(target=print(f'Массив чисел (по убыванию): {sorted(array_descending, reverse=True)}'))
thread2 = Thread(target=print(f'Массив чисел (по возрастанию): {sorted(array_ascending)}'))
thread3 = Thread(target=print(f'Массив символов (лексикографический порядок): {sorted(symbols_array)}'))

