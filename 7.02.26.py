# def a():
#     print("Hello world")
# a()
# print("Hello again")
import asyncio


# процессы (ресурсы / память / файлы / соединения) -->
# Потоки --> (ресурсы от процесса / быстрее создаются и переключаются / могут обмениваться данными)

# Важность процессов -->
# сварить макароны - пожарить мясо
# варить макароны 4 мин
# пожарить мясо 4 мин
# 8мин

# варить макароны 2 мин
# пожарить мясо в течение макарон --> (3 мин)

# Параллелизм
# 2 мин --> ядра процессора


# import asyncio
#
# # async with async for
# async def f():
#     print("Hello")
#     await asyncio.sleep(1)
#     print("Goodbye")
#
# asyncio.run(f())

# def sync_f():
#     return "Результат"
#
# async def async_f():
#     data = [1,2,3]
#     print(sum(data))
#     return "Результат"
#
# print(sync_f())
# # print(async_f())
# asyncio.run(async_f())

# import asyncio
#
# async def one(num):
#     print("f_1 start")
#     await asyncio.sleep(num)
#     print("f_1 end")
#
# async def two(num):
#     print("f_2 start")
#     await asyncio.sleep(num)
#     print("f_2 end")
#
# async def main():
#     results = await asyncio.gather(one(10), two(1))
#     # task1 = asyncio.create_task(one())
#     # task2 = asyncio.create_task(two())
#     # while True:
#     #     await asyncio.sleep(1)
#     #     task1.cancel()
#     #     print("abcde")
#         # if task1.cancelled():
#         # if task1.done():
#     # result1 = await task1
#     # result2 = await task2
#
# asyncio.run(main())

# import asyncio
#
# async def download_page(url):
#     print(f"Загружаю {url}")
#     await asyncio.sleep(1)
#     return f"содержимое {url}"
#
# async def main():
#     urls = [
#         "https://www.baidu.com/",
#         "https://www.sausage.com/",
#         "https://www.baid.com/",
#         "https://www.sausage.com/",
#         "https://www.bai.com/",
#         "https://www.sasage.com/",
#     ]
#     task = asyncio.create_task(download_page(urls[0]))
#     await asyncio.gather(task)
#     pages = await asyncio.gather(*[download_page(url) for url in urls])
#     print(f'загружено {len(pages)} страниц')
#     for content in pages:
#         print(content)
# asyncio.run(main())
#
#
#
#
# import time
# import asyncio
# async def make_coffe():
#     await asyncio.sleep(2)
#     print("Coffee is ready")
#
# async def make_toast():
#     await asyncio.sleep(2)
#     print("Toast is ready")
# start = time.time()
#
# async def main():
#     await make_coffe()
#     await make_toast()
# asyncio.run(main())
# finish = time.time() - start
# print(finish)