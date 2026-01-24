# def calculator(x,y,lambda1, lambda2):
#     a = [
#     (lambda1(x,y)),
#     (lambda2(x,y))
#     ]
#     return a
# print(calculator(
#     10, 4,
#     lambda1 = lambda x,y : x+y,
#     lambda2 =lambda x,y : x-y
# ))

## MAP
# map это метод который позвлояет применить функцию к любому элементу поледовательности
# map(,список(итерируемый объект))
# def plus5(x):
#     return x + 5
# a =
# print(list(map(plus5, a)))
# print(list(map(lambda x :x + 5, a)))

# user = [
#     {"username":"petya1", "age": 10},
#     {"username":"petya2", "age": 15},
#     {"username":"petya3", "age": 16}
# ]
# print(list(map(lambda x: x["username"], user)))

# nums = list(range(1,11))
# nums = ['1', '2', '3']
# evens = list(filter(lambda x: int(x) == 0, nums))
# print(nums)
# print(evens)
# def plus():
#     return "+"
# def minus():
#     return "-"
# def nums(fplus, fminus):
#     return fplus(), fminus()
# print(nums(plus, minus))

# nums = [1,2,3,4,5]
# a = list(map(lambda x: x**2, nums))

# nums = [1,2,3,4,5,6,7,8,9,10]
# a = list(filter(lambda num: num % 2 == 0, nums))
# print(a)

# words = ['apple', 'banana', 'cherry', 'date']
# a = list(map(lambda x: len(x), words))
# print(a)

# nums = [-5, -2, 0, 3, 7, -1, 10]
# a = list(filter(lambda x: x > 0, nums))

# a = [1,1,1,1,1,1,1,1]
# b = [2,2,2,2,2,2,2,2]
# print(map(lambda x, y : x + y, a,b))

# list1 = [1,2,3,4]
# list2 = [5,6,7,8]
# print(list(map(lambda x,y : x*y, list1, list2)))

# nums = [1,2,3,4,5,6,7,8,9, 10,11,12]
# not_prime_nums = list(filter(lambda num: num%2 == 0 or num%3 == 0 or num%5 == 0 or num & 7 == 0 , nums))

# def my_map(func, iterable):
#     result = []
#     for item in iterable:
#         result.append(func(item))
#     return result
# nums = ["hello"]
# print(my_map(len, nums))


