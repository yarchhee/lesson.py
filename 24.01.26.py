# def a():
#     def b():
#         print("Hello World")
#     b()

# def a(text):
#     def b(t):
#         print(t + text)
#     hello = "124"
#     return b("hello")
# print(hello)
# b("hello")
# a("world")

# def a(name,func):
#     print(name)
# a("борис", lambda x: x * 2)

# def create_discount(category):
#     def bronze(price):
#         return price * 2
#
#     def silver(price):
#         return price * 0.5
#
#     def gold(price):
#         return price * 0.1
#
#     if category == 'bronze':
#         return bronze
#     elif category == 'silver':
#         return silver
#     elif category == 'gold':
#         return gold
#
#
# bronze_discount = create_discount('bronze')
# product_price = 1000


# def count_10_times(nums):
#     if nums >= 10:
#         return nums
#     return count_10_times(nums +1)
# count_10_times(1)


# name = "hello"
# def a():
#     global name
#     name2 = "world"
#     def next():
#         nonlocal name
#     next()
#     print(name2)
# a()

# def create_adder(number):
#     def add_to(x):
#         return x + number
#     return add_to
#
# add_five = create_adder(5)
#
# add_ten = create_adder(10)
#
# print(add_five(5))
# print(add_ten(10))
# def make_even_generator(start):
#
#     def next_even():
#         nonlocal start
#         result = start
#         start += 2
#         return result
#     return next_even
# even_gen = make_even_generator(6)
# print(even_gen())

# def make_string_builder(st):
#     def the_string(x):
#         nonlocal st
#         result = st
#         st += x
#         return result
#     return the_string
# a = make_string_builder('abc')
# print(a)
# print(a)

# def make_product_accumulator(start):
#     def product_accumulator(p):
#         nonlocal start
#         result = start * p
#         return result
#     return product_accumulator
# a = make_product_accumulator(3)
# print(a(5))
# print(a(6))

# def make_counter(start, step):
#     def adder():
#         nonlocal start
#         start += step
#         return start
#     return adder
# a = make_counter(1, 2)
# print(a())
# print(a())

# def create_length_filter(min_length):
#     def length_filter(word):
#         return len(word) >= min_length
#     return length_filter
# a = create_length_filter(5)
# print(a('hel'))
# print(a('hello'))






