from threading import Thread
from string import ascii_lowercase


def main():
    def print_d():
        for i in range(1, 6):
            print(i)
    def print_a():
        for a in ascii_lowercase[:5]:
            print(a)
    thread_1 = Thread(target=print_d)
    thread_2 = Thread(target=print_a)
    thread_1.start()
    thread_1.join()
    thread_2.start()
    thread_2.join()

if __name__ == '__main__':
    main()
    print('Готово!')