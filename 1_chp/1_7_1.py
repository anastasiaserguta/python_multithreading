from threading import Thread
from time import sleep

def first_def(name):
    print(f'Поток {name} запустился.')
    sleep(2)

def second_def(name):
    print(f'Поток {name} запустился.')
    sleep(3)

def main():
    thread_1 = Thread(target=first_def, name='A', args='A')
    thread_2 = Thread(target=second_def, name='B', args='B')
    thread_1.start()
    thread_1.join(timeout=2.1)
    thread_2.start()
    if thread_1.is_alive() == True:
        print(f'Поток {thread_1.name} не завершился за установленное время.')
    elif thread_2.is_alive() == True:
        print(f'Поток {thread_2.name} не завершился за установленное время.')

if __name__ == '__main__':
    main()