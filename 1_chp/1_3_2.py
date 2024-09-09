from threading import Thread
from math import prod


def sum_total(*args):
    print(f"Сумма чисел от 1 до 1000: {sum(args)}")

def mul_total(*args):
    print(f"Произведение чисел от 1 до 10: {prod(args)}")

thread_1 = Thread(target=sum_total, args=range(1, 1001))
thread_2 = Thread(target=mul_total, args=range(1, 11))

thread_1.start()
thread_2.start()