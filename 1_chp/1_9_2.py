from threading import Thread, local, current_thread
from time import sleep

storage = local()

students_info = {'Варлаам Бирюкова': {'Возраст': 25, 'Специальность': None, 'Город': None, 'Страна': 'Россия',
                                      'Университет': 'ЗАО «Миронова-Прохоров»', 'Курс': 3, 'Группа': 'CK008',
                                      'Электронная почта': 'ostaplitkin@example.com', 'Телефон': None,
                                      'Дата рождения': '2005-08-22', 'Пол': 'Женский',
                                      'Хобби': ['Физика', 'Астрономия'], 'Время обработки': 6},
                 'Никандр Мамонтов': {'Возраст': 20, 'Специальность': 'Компьютерные науки',
                                      'Город': 'к. Октябрьский (Башк.)', 'Страна': 'Россия', 'Университет': None,
                                      'Курс': 3, 'Группа': 'LE057', 'Электронная почта': 'jakub_2001@example.org',
                                      'Телефон': '+7 919 424 9512', 'Дата рождения': '2002-01-13', 'Пол': None,
                                      'Хобби': None},}

def thread_function(name_s, info):
    storage.sleep_time = info.get('Время обработки', 3)
    sleep(storage.sleep_time/10)
    for i in info.keys():
        if info[i] is None:
            continue
        storage.data = f'{i}: {info[i]}'
        print(f"Имя потока - {current_thread().name}, локальные данные потока - {storage.data}")

for st in students_info.keys():
    thread = Thread(target=thread_function, name=st, args=(st, students_info[st],))
    thread.start()