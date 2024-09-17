from threading import Thread, enumerate, current_thread
from time import sleep

delays = [1, 3, 4, 5, 2]

def my_task(t):
    print(f'Поток {current_thread().name} начал работу')
    sleep(int(t))
    print(f'Поток {current_thread().name} завершил работу')


def main():
    for t in delays:
        thread = Thread(target=my_task, args=(int(t),))
        thread.start()

sleep(1.5)

main()
for thr in enumerate():
    print(f'{thr.name} еще выполняется')