"""# Импортируем модуль multiprocessing для многопроцессорности
# Импортируем модуль requests для HTTP-запросов
# Импортируем модуль time для измерения времени выполнения
# Импортируем модуль tracemalloc для профилирования памяти
# Импортируем модуль psutil для получения информации о системе
# Импортируем модуль logging для логирования
# Настройка логирования
# Функция для загрузки данных
# Выполняем синхронный GET-запрос
# Возвращаем текст ответа
# Основная функция с использованием пула процессов
# Ограничиваем количество процессов
# Используем пул процессов
# pool.map автоматически распределяет задачи между процессами
# Функция профилирования
# Повторяем URL для теста
# Запуск профилирования памяти
# Начало отсчета времени
# Запуск многопроцессорной функции
# Окончание отсчета времени
# Получение информации о текущем процессе
# Получение использования памяти в МБ
# Логирование времени выполнения и использования памяти
# Запуск функции профилирования"""
import multiprocessing
import requests
import time
import tracemalloc
import psutil
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def fetch(url):
    logging.info(f"Fetching {url}")
    response = requests.get(url)
    return response.text


def multiprocessing_main(urls):
    num_processes = min(50, len(urls))
    logging.info(f"Starting multiprocessing with {num_processes} processes")

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(fetch, urls)

    return results


def profile_multiprocessing():
    urls = ["https://www.example.com"] * 100

    tracemalloc.start()

    start_time = time.time()
    multiprocessing_main(urls)
    end_time = time.time()

    process = psutil.Process()
    mem_usage = process.memory_info().rss / (1024 * 1024)

    logging.info(f"Multiprocessing I/O time: {end_time - start_time:.2f} seconds")
    logging.info(f"Memory usage: {mem_usage:.2f} MB")


if __name__ == '__main__':
    profile_multiprocessing()
