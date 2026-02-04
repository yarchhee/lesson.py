# from time import time
# from unittest import result
#
# start = time()
# def fib(n):
#     if n<2:
#         return n
#     return fib(n-1) + fib(n-2)
# print(fib(10))
# print(time() - start)


# s = {}
# def fib(n):
#     if n in s:
#         return s[n]
#     if n<2:
#         return n
#     result =  fib(n-1) + fib(n-2)
#     s[n] = result
#     return result

from functools import lru_cache
# @lru_cache():
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n - 1) + fib(n - 2)


# стек - LIFO - last in first out - пирамида
# очередь - FIFO - first in first out
# LFU - least frequency used - библиотека
# LRU = least recently used - наименьшее недавно использованный

import sys
sys.setrecursionlimit(10000)
# def f(n):
#     if n<5:
#         return n
#     return 2 * n * f(n-4)
# print((f(13766)- 9 * f(13762)) / f(13758))

# def f(n):
#     if n == 1:
#         return 1
#     elif n>1:
#         return 2*n*f(n-1)
# print((f(2024)//16 - f(2023)) / f(2022))

@lru_cache()
def tribonacci(n):
    if n <2:
        return n
    if n == 2:
        return 1
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
print(tribonacci(10))