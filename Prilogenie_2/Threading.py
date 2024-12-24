"""# Импортируем модуль threading для многопоточности
# Импортируем модуль time для измерения времени выполнения
# Импортируем модуль tracemalloc для профилирования памяти
# Импортируем модуль psutil для получения информации о системе
# Функция для вычисления числа Фибоначчи
# Функция для выполнения вычислений в потоке
# Выполняем вычисление и сохраняем результат
# Основная функция
# Список чисел для вычисления
# Создаем список для хранения результатов
# Список для хранения потоков
# Проходим по каждому числу
# Создаем поток для выполнения функции
# Добавляем поток в список
# Запускаем поток
# Ожидаем завершения всех потоков
# Запуск профилирования памяти
# Начало отсчета времени
# Запуск многопоточной функции
# Окончание отсчета времени
# Получение информации о текущем процессе
# Получение использования памяти в МБ
# Вывод времени выполнения
# Вывод использования памяти
# Запуск функции профилирования"""
import threading
import time
import tracemalloc
import psutil


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def threaded_fibonacci(n, results, index):
    results[index] = fibonacci(n)


def threaded_main():
    numbers = [30, 32, 34]
    results = [None] * len(numbers)
    threads = []

    for i, number in enumerate(numbers):
        thread = threading.Thread(target=threaded_fibonacci,
                                  args=(number, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def profile_threading_computation():
    tracemalloc.start()

    start_time = time.time()
    threaded_main()
    end_time = time.time()

    process = psutil.Process()
    mem_usage = process.memory_info().rss / (1024 * 1024)

    print("Threading computation time:", end_time - start_time)
    print(f"Memory usage: {mem_usage:.2f} MB")


profile_threading_computation()
