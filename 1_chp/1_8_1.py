from threading import Thread, current_thread
from time import sleep

code_names = ['Delta', 'NotDelta']

def task(name):
    current_thread().name = name
    print(f'Новое имя потока: {current_thread().name}')
    print(f'Задача выполнена для {current_thread().name}')

def main():
    for name in code_names:
        thread = Thread(target=task, args=(name,))
        print(f'Исходное имя потока: {thread.name}')
        thread.start()
        thread.join()

main()