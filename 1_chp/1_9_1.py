from threading import Thread, local

def process_data(data):
    thread_data.data = data
    print(f"Данные в локальном хранилище: {thread_data.data}")

thread_data = local()


for i in range(3):
    data = 'HELLO LOCAL STORAGE!'
    thread = Thread(target=process_data, args=(data,))
    thread.start()