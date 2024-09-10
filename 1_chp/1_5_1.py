from threading import Thread
from time import sleep

def digits_1():
    for i in range(1, 6):
        print(i)
        sleep(0.5)
        
def digits_2():
    for t in range(6, 11):
        print(t)
        sleep(1)

thread_1 = Thread(target=digits_1)
thread_2 = Thread(target=digits_2)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()

print('Оба потока завершили свою работу.')