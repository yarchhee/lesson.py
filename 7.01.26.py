# count / find / rfind / (is)lower / (is)upper
# set / bool / int / str / tuple / list / float / dict / None
# sort / sorted
# [::-1] reversed
# replace
# type

# if elif else

# match case

# for while

# def name():
#     print(123)

# x = input().split()
# d = ""
# for i in x:
#     d+= i[::-1]
#     d+= "  "
# print(d)

# all()
# any()

# print(any([True, False])) # or
# print(all([True, False, True])) #  and

# a = []
# for i in range(1, 10):
#     a.append(i % 10 == 0)
# print(any(a))
# print(all(a))

# a = [10, 20, 30, 40, 50, -1]
# b = []
# for i in a:
#         b.append(i >= 0)
# print(all(b))

# a = ['', 'hello', '', 'world']
# b = []
# for i in a:
#     b.append(i != "")
# print(all(b))

# enumerate(последовательность, начальный индекс)
# print(list(enumerate(["h","e",'l','l'], start = 0)))

# a = ['h', 'e', 'l' ]
# for i, item in enumerate(a, start = 0):
#     print(i, item)

# my_dict = {
#     "key 1":'it 1',
#     "key 2":'it 2',
#     "key 3":'it 3'
# }
# for key, value in my_dict.items():
#     print(key, value)
# for i, (key, value) in enumerate(my_dict, start = 1):
#     print(i, key, value)

# *
# a = ([1,2,3,4,5],(6,7,8,9,10))
# (z, *y), (k, *s) = a #пакуем элементы
# print(k, s)
# print(z, y)

# print(*a[0], sep = "")

# a = [10, 25, 30, 15, 40, 5, 50]
# for i, item in enumerate(a, start = 0):
#     if item > 20:
#         print(i, item)

# a = ["python", "java", "c", 'javascript', 'go', 'rust', 'php']
# for i , item in enumerate(a):
#     if item.find("a") != -1 and len(a)>3:
#         print(i,item)

# zip()
# a = ["hello", 'my name is ']
# b = ['world', 'Yarik']
# for first, second in zip(a, b):
#     print(first, second)
# print(list(zip(a, b)))
# pairs = [(1, 'a'),(2,'b'),(3,'c'),(4,"d")]
# nums, letters = zip(*pairs)
# print(nums)
# print(letters)
# names = ['Alexey', "Maria", 'Ivan']
# ages = [25,30,22]
# for name, age in zip(names, ages):
#     print(f'{name}:{age}')

# students = ['Анна', 'Борис', 'Виктор']
# subjects = ['Математика', 'Физика', 'Химия']
# grades = [5, 4, 5]
# for students, subjects, grades in zip(students, subjects, grades):
#     print(f'{students} - {subjects} - {grades}')

prices = [100, 200, 150, 300]
discount = [10, 15, 5, 20]
for price, disc in zip(prices, discount):
    print(price - (disc/price *100))
