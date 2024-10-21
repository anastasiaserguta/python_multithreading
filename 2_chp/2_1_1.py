from concurrent.futures import ThreadPoolExecutor
# Список строк для обработки
strings = [
    "Да Здравствует ThreadPoolExecutor!!!",
    "Многопоточность в Python позволяет выполнять несколько задач одновременно, улучшая производительность.",
    "Многопоточность может увеличить сложность управления памятью и ресурсами.",
    "Правильное использование многопоточности в Python может значительно улучшить производительность приложений."
]

def to_uppercase(string):
    return string.upper()

with ThreadPoolExecutor(max_workers=2) as executor:
    for sent in strings:
        future = executor.submit(to_uppercase, sent)
        print(future.result())
    
    
    
    

    
    