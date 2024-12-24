"""# Импортируем модуль threading для многопоточного выполнения
# Импортируем модуль time для измерения времени выполнения
# Импортируем модуль tracemalloc для профилирования использования памяти
# Импортируем модуль psutil для получения информации о системе и процессе
# Функция для обработки задачи
# Блокирующая задержка на 0.1 секунды
# Основная функция для выполнения задач с использованием threading
# Список для хранения потоков
# Создаем и запускаем 1000 потоков
# Создаем поток для выполнения задачи
# Добавляем поток в список
# Запускаем поток
# Ждем завершения всех потоков
# Блокируем выполнение до завершения текущего потока
# Функция для профилирования многопоточного выполнения
# Начинаем профилирование использования памяти
# Фиксируем время начала выполнения
# Запускаем основную функцию с threading
# Фиксируем время завершения выполнения
# Получаем информацию о текущем процессе
# Получаем использование памяти в МБ
# Выводим использование памяти
# Запускаем функцию профилирования для threading"""
import threading
import time
import tracemalloc
import psutil


def process_task(n):
    time.sleep(0.1)


def threaded_main():
    threads = []

    for i in range(1000):
        thread = threading.Thread(target=process_task, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def profile_threading_parallelism():
    tracemalloc.start()

    start_time = time.time()
    threaded_main()
    end_time = time.time()

    process = psutil.Process()
    mem_usage = process.memory_info().rss / (1024 * 1024)

    print("Threading parallelism time:", end_time - start_time)
    print(f"Memory usage: {mem_usage:.2f} MB")


profile_threading_parallelism()
