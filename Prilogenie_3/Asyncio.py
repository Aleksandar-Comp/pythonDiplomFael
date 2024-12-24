"""# Импортируем модуль asyncio для асинхронного программирования
# Импортируем модуль time для измерения времени выполнения
# Импортируем модуль tracemalloc для профилирования использования памяти
# Импортируем модуль psutil для получения информации о системе и процессе
# Блокирующая функция для обработки задачи
# Блокирующая задержка на 0.1 секунды
# Возвращаем значение i после выполнения задачи
# Асинхронная функция для выполнения блокирующих задач
# Получаем текущий событийный цикл
# Запуск 1000 задач в блокирующем режиме через executor
# Ожидаем завершения всех задач и собираем результаты
# Функция для профилирования асинхронного выполнения с блокирующими задачами
# Начинаем профилирование использования памяти
# Фиксируем время начала выполнения
# Запускаем асинхронную функцию с блокирующими задачами
# Фиксируем время завершения выполнения
# Получаем информацию о текущем процессе
# Получаем использование памяти в МБ
# Выводим время выполнения
# Выводим использование памяти
# Запускаем функцию профилирования для asyncio"""
import asyncio
import time
import tracemalloc
import psutil


def blocking_task(i):
    time.sleep(0.1)
    return i


async def async_main():
    loop = asyncio.get_event_loop()

    tasks = [loop.run_in_executor(None, blocking_task, i) for i in range(1000)]
    return await asyncio.gather(*tasks)


def profile_asyncio_parallelism():
    tracemalloc.start()

    start_time = time.time()
    asyncio.run(async_main())
    end_time = time.time()

    process = psutil.Process()
    mem_usage = process.memory_info().rss / (1024 * 1024)

    print("Asyncio (blocking) parallelism time:", end_time - start_time)
    print(f"Memory usage: {mem_usage:.2f} MB")


profile_asyncio_parallelism()
