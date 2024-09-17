from threading import Timer

astronauts = ["Алексей Леонов", "Юрий Гагарин", "Джон Гленн"]
tasks = ["Ремонт оборудования", "Проведение экспериментов", "Мониторинг систем"]
intervals = [0.7, 1.3, 1.8]

def task(name, task):
    print(f'{name} выполняет задачу: {task}')

for i in range(len(astronauts)):
    timer = Timer(intervals[i], task, args=(astronauts[i], tasks[i],))
    timer.start()