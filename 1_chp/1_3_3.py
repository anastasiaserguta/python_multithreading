from threading import Thread
# Массив чисел для обработки
numbers = [456, 467, 961, 561, 512, 740, 6412, 464, 444, 102, 456, 347, 905, 854, 901, 326, 267, 236, 790, 235, 745,
           769, 467, 734, 745, 895, 445, 312, 123, 451, 523, 567, 344, 234]

# Создайте потоки
thread_even = Thread(target=print(f'Сумма четных чисел: {sum(num for num in numbers if num % 2 == 0)}'))
thread_odd = Thread(target=print(f'Сумма нечетных чисел: {sum(num for num in numbers if num % 2 != 0)}'))

# Запустите потоки
thread_even.start()
thread_odd.start()

