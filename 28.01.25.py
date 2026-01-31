


# def add_with_logging(a,b):
#     result = add(a,b)
#     print(f"Выполнилась функция add: a = {a}, b = {b}, a+b = {a + b}")
#     return result
#
# def mul_with_logging(a,b):
#     result = mul(a,b)
#     print(f"Выполнилась функция mul: a = {a}, b = {b}, a*b = {a * b}")
#     return result

def create_logging_wrapper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Вызвана функция {func.__name__} с аргументом {args}, результат: {result}")
        return result
    return wrapper

@create_logging_wrapper
def add(a, b):

    return a + b

@create_logging_wrapper
def mul(a, b):

    return a * b
print(add(2, 3))
print(mul(2, 3))

# add_w_logging = create_logging_wrapper(add)
# mul_w_logging = create_logging_wrapper(mul)
# print(add_w_logging(1,2))
# print(mul_w_logging(3, 2))

# import time
#
# start = time. time()
#
# a = 1 + 1 #1.6
#
# end = time.time()
#
# print(end - start)
# start = time. time()
# for i in range (10000): #1.6 - 0.0004 = ...
#     print(i)
# end = time.time ()
# print(end - start)

from time import time
def timeit_func(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(args)
        print(time() - start)
        return result
    return wrapper
@timeit_func
def add(nums:list):
    summ = 0
    for num in nums:
        summ += num
    return summ

@timeit_func
def mul(nums:list):
    mullt = 1
    for num in nums:
        mullt *= num
    return mullt

a = mul([1,2,3,4,5])
print(a)

def parent(func):
    def wrapper(*args, **kwargs):
        start = time()
        a = func(*args)
        print(time() - start, a)
        return a
    return wrapper

@parent
def test(tfunc, list_nums):
    for i, num in enumerate(list_nums):
        list_nums[i] = tfunc(num)
    return list_nums

a = test(lambda x: x**3, [1,2,3])
print(a)





