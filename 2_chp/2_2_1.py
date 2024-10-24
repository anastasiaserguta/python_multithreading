from concurrent.futures import ThreadPoolExecutor

list1 = ['kw63vdxI', 'YmSsWblC', '5OJ3Mto9']
list2 = ['7GBrUY6t', 'bfQjS3gj', 'MhTsKf0X']
list3 = ['mt05f80F', 'haHHiXoX', 'v2cYPhRO']


# Функция воркера, которая печатает сообщение из списка        
def worker(texts, thread_num):
    for word in texts:
        print(f'Поток {thread_num} извлёк текст из списка: {word}')


# Использование ThreadPoolExecutor для параллельного выполнения
with ThreadPoolExecutor(max_workers=3) as executor:
    for i in range(1, 4):
        future = executor.submit(worker, texts=eval(f'list{i}'), thread_num=i)
