from threading import Thread, main_thread

for i in range(1, 100):
    a = i

thread = main_thread()
print(f'Имя главного потока по умолчанию: {thread.name}')

thread.name = 'My_main_thread'
print(f'Новое имя главного потока: {thread.name}')

print(f'Демонический признак главного потока: {thread.daemon}') 
