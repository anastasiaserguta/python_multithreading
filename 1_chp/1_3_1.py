from threading import Thread

# Список для суммирования
numbers = [123456, 7890123, 987654, 114455, 995423, 1000000]

# Функция для потока, обрабатывающего список
def thread_task():
    print(sum(numbers))


# Создайте поток
thread = Thread(target=thread_task)

# Запустите поток
thread.start()

# Дождитесь завершения потока
thread.join()
