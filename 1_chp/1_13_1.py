from threading import Timer

# Инициализация параметров аукциона

initial_bid = 25     # Начальная ставка аукциона. С этой суммы начинается аукцион.
bid_increment = 5   # Сумма, на которую увеличивается текущая ставка на каждом шаге аукциона.
max_bid = 40          # Максимальная ставка, при достижении которой аукцион завершается.
interval = 2      # Интервал времени (в секундах) между увеличениями ставок.

# Допишите функцию увеличения ставки    
def increase_bid(start, plus, maxim):
    print(f"Текущая ставка: {start} у.е.")
    if start >= maxim:
        return 
    start += plus
    timer = Timer(interval, increase_bid, args=(start, plus, maxim))
    timer.start()
    timer.join()


# Вызовите эту функцию
increase_bid(initial_bid, bid_increment, max_bid)
print('Ставок нет, аукцион завершен!')
