"""# Импортируем модуль multiprocessing для многопроцессорного выполнения
# Импортируем модуль time для измерения времени выполнения
# Импортируем модуль tracemalloc для профилирования использования памяти
# Импортируем модуль psutil для получения информации о системе и процессе
# Функция для обработки задачи
# Блокирующая задержка на 0.1 секунды
# Основная функция для выполнения задач с использованием multiprocessing
# Список для хранения процессов
# Создаем и запускаем 1000 процессов
# Создаем процесс для выполнения задачи
# Добавляем процесс в список
# Запускаем процесс
# Ждем завершения всех процессов
# Блокируем выполнение до завершения текущего процесса
# Функция для профилирования многопроцессорного выполнения
# Начинаем профилирование использования памяти
# Фиксируем время начала выполнения
# Запускаем основную функцию с multiprocessing
# Фиксируем время завершения выполнения
# Получаем информацию о текущем процессе
# Получаем использование памяти в МБ
# Выводим время выполнения
# Выводим использование памяти
# Запускаем функцию профилирования для multipr"""
import multiprocessing
import time
import tracemalloc
import psutil


def process_task(n):
    time.sleep(0.1)


def multiprocessing_main():
    processes = []

    for i in range(1000):
        process = multiprocessing.Process(target=process_task, args=(i,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


def profile_multiprocessing_parallelism():
    tracemalloc.start()

    start_time = time.time()
    multiprocessing_main()
    end_time = time.time()

    process = psutil.Process()
    mem_usage = process.memory_info().rss / (1024 * 1024)

    print("Multiprocessing parallelism time:", end_time - start_time)
    print(f"Memory usage: {mem_usage:.2f} MB")


if __name__ == '__main__':
    profile_multiprocessing_parallelism()
