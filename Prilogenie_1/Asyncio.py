"""# Импортируем модуль asyncio для асинхронного программирования
# Импортируем модуль aiohttp для асинхронных HTTP-запросов
# Импортируем модуль time для измерения времени выполнения
# Импортируем модуль tracemalloc для профилирования памяти
# Импортируем модуль psutil для получения информации о системе
# Асинхронная функция для загрузки данных
# Создаем асинхронную сессию HTTP
# Выполняем асинхронный GET-запрос
# Возвращаем текст ответа
# Основная асинхронная функция
# Создаем список задач для загрузки данных
# Запускаем все задачи параллельно и ждем их завершения
# Функция для профилирования выполнения
# Повторяем URL для теста
# Запуск профилирования памяти
# Начало отсчета времени
# Запуск асинхронной функции
# Окончание отсчета времени
# Получение информации о текущем процессе
# Получение использования памяти в МБ
# Вывод времени выполнения
# Вывод использования памяти
# Запуск функции профилирования"""
import asyncio
import aiohttp
import time
import tracemalloc
import psutil


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def async_main(urls):
    tasks = [fetch(url) for url in urls]
    return await asyncio.gather(*tasks)


def profile_asyncio():
    urls = ["https://www.example.com"] * 100

    tracemalloc.start()

    start_time = time.time()
    asyncio.run(async_main(urls))
    end_time = time.time()

    process = psutil.Process()
    mem_usage = process.memory_info().rss / (1024 * 1024)

    print("Asyncio I/O time:", end_time - start_time)
    print(f"Memory usage: {mem_usage:.2f} MB")


profile_asyncio()
