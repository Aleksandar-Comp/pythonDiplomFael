"""# Импортируем модуль threading для многопоточности
# Импортируем модуль requests для HTTP-запросов
# Импортируем модуль time для измерения времени выполнения
# Импортируем модуль tracemalloc для профилирования памяти
# Импортируем модуль psutil для получения информации о системе
# Функция для загрузки данных
# Выполняем синхронный GET-запрос
# Сохраняем текст ответа в список
# Основная функция
# Создаем список для хранения результатов
# Список для хранения потоков
# Проходим по каждому URL
# Создаем поток для выполнения функции
# Добавляем поток в список
# Запускаем поток
# Ожидаем завершения всех потоков
# Повторяем URL для теста
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
import requests
import time
import tracemalloc
import psutil


def fetch(url, results, index):
    response = requests.get(url)
    results[index] = response.text


def threaded_main(urls):
    results = [None] * len(urls)
    threads = []

    for i, url in enumerate(urls):
        thread = threading.Thread(target=fetch, args=(url, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def profile_threading():
    urls = ["https://www.example.com"] * 100

    tracemalloc.start()

    start_time = time.time()
    threaded_main(urls)
    end_time = time.time()

    process = psutil.Process()
    mem_usage = process.memory_info().rss / (1024 * 1024)

    print("Threading I/O time:", end_time - start_time)
    print(f"Memory usage: {mem_usage:.2f} MB")


profile_threading()
