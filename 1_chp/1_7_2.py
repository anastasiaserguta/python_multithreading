from threading import Thread, current_thread
from time import sleep

name_threads = ['OF95RK', 'VH61DX', 'NB03WA', 'WO40ZF', 'NJ48EG', 'SX21ET', 'AT01PA', 'MR36DD', 'DD84HR', 'MI81QY']

def worker():
    thread_name = current_thread().name
    print(f'{thread_name} начал работу.')
    sleep(1)
    
for n in name_threads:
    thread = Thread(target=worker, name=f'Name_thread-{n}')
    thread.start()
    thread.join()
    print(f'{thread.name} завершил работу.')
