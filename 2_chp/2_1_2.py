from concurrent.futures import ThreadPoolExecutor

# Функция для вычисления суммы чисел в заданном диапазоне
def sum_range(start, end):
    return sum(range(start, end + 1))

# Создание пула потоков
with ThreadPoolExecutor(max_workers=3) as executor:
    future_1 = executor.submit(sum_range, 1, 100)
    future_2 = executor.submit(sum_range, 101, 200)
    future_3 = executor.submit(sum_range, 201, 300)

    sum1 = future_1.result()
    sum2 = future_2.result()
    sum3 = future_3.result()

    print(f"Сумма чисел от 1 до 100: {sum1}")
    print(f"Сумма чисел от 101 до 200: {sum2}")
    print(f"Сумма чисел от 201 до 300: {sum3}")