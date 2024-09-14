from threading import Thread, current_thread
from time import sleep

res = []

# Функция для имитации загрузки файла
def load_file(file_name):
    res.append(f'{current_thread().name} начал загрузку файла {file_name}.')
    res.append(f'{current_thread().name} завершил загрузку файла {file_name}.')


# Функция для имитации обработки файла
def process_file(file_name):
    res.append(f'{current_thread().name} начал обработку файла {file_name}.')
    res.append(f'{current_thread().name} завершил обработку файла {file_name}.')


# Функция для имитации сохранения файла
def save_file(file_name):
    res.append(f'{current_thread().name} начал сохранение файла {file_name}.')
    res.append(f'{current_thread().name} завершил сохранение файла {file_name}.')

file_names = ['file623.xlsx', 'file538.jpg', 'file11.rar', 'file180.jpg', 'file984.docx', 'file931.rar', 'file600.zip', 'file928.jpg', 'file899.pdf', 'file763.png', 'file601.txt', 'file194.pdf', 'file307.rar', 'file961.jpg', 'file539.mp4', 'file44.docx', 'file276.zip', 'file387.zip', 'file520.xlsx', 'file516.mp3', 'file802.jpg', 'file708.mp3', 'file100.xlsx', 'file327.xlsx', 'file451.zip', 'file125.pdf', 'file477.jpg', 'file432.pdf', 'file569.docx', 'file990.mp3', 'file688.mp3', 'file735.docx', 'file505.txt', 'file650.docx', 'file445.png', 'file963.mp4', 'file583.pdf', 'file403.xlsx', 'file406.pdf', 'file187.txt', 'file13.zip', 'file495.docx', 'file47.png', 'file491.rar', 'file506.zip', 'file960.docx', 'file95.mp3', 'file566.jpg', 'file66.rar', 'file13.txt']

for file in file_names:
    thread_1 = Thread(target=load_file, name=f'LoadThread-{file}', args=(file,))
    thread_1.start()
    thread_1.join()
    thread_2 = Thread(target=process_file, name=f'ProcessThread-{file}', args=(file,))
    thread_2.start()
    thread_2.join()
    thread_3 = Thread(target=save_file, name=f'SaveThread-{file}', args=(file,))
    thread_3.start()
    thread_3.join()


for s in res:
    print(s)

print(res)