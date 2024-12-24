"""# Импортируем модуль asyncio для асинхронного программирования
# Импортируем модуль time для измерения времени выполнения
# Импортируем модуль tracemalloc для профилирования памяти
# Импортируем модуль psutil для получения информации о системе
# Функция для вычисления числа Фибоначчи
# Асинхронная функция для выполнения вычислений
# Получаем текущий событийный цикл
# Выполняем вычисление в отдельном потоке
# Основная асинхронная функция
# Список чисел для вычисления
# Создаем задачи для вычисления
# Запускаем все задачи параллельно и ждем их завершения
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
import time
import tracemalloc
import psutil


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


async def async_fibonacci(n):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, fibonacci, n)


async def async_main():
    numbers = [30, 32, 34]
    tasks = [async_fibonacci(n) for n in numbers]
    return await asyncio.gather(*tasks)


def profile_asyncio_computation():
    tracemalloc.start()

    start_time = time.time()
    asyncio.run(async_main())
    end_time = time.time()

    process = psutil.Process()
    mem_usage = process.memory_info().rss / (1024 * 1024)

    print("Asyncio computation time:", end_time - start_time)
    print(f"Memory usage: {mem_usage:.2f} MB")


profile_asyncio_computation()
