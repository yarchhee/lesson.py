#Задача 46
# t = (5,5,5,5,1,1,1,2,2,3,4,5)
# count = 1
# maxim = 0
# for i in range(1, len(t)):
#     if t[i] == t[i-1]:
#         count += 1
#     else:
#         if maxim < count:
#             maxim = count
#         count = 1
# print(maxim)

#Задача 47
# cart = [("яблоки", 100), ("хлеб",50),("молоко",80),("яблоки", 100)]
# cart1 = []
# cart2 = []
# cart3 = []
# for i,j in cart:
#     if j > 70:
#         cart1.append((i,j))
# print(cart1)
# for i,j in cart:
#     cart2.append((i,j*2))
# print(cart2)
# for i,j in set(cart):
#     cart3.append((i,j/2))
# print(cart3)

#Задача 48
# books = [("Война и мир", 1865), ("1984", 1949), ("Гарри Поттер", 1997), ("Война и мир", 1865)]
# books1 = []
# books2 = []
# books3 = []
# for i,j in books:
#     if j>1900:
#         books1.append(i)
# for i,j in books:
#     books2.append(j-100)
# for i,j in books:
#     if j<1950:
#         books3.append(("Классика:",i,j))
#     else:
#         books3.append((i,j))
# print(books1)
# print(books2)
# print(books3)

#Задача 59
# math_students = {"Анна", "Борис", "Вера", "Глеб"}
# physics_students = {"Борис", "Вера", "Дмитрий", "Елена"}
# chemistry_students = {"Вера", "Глеб", "Дмитрий", "Жанна"}
# mandp = math_students.intersection(physics_students)
# mandpandc = mandp.intersection(chemistry_students) # & - то же самое
# print(mandpandc)
# monly = math_students.difference(physics_students) # - = то же самое
# monlyonly = monly.difference(chemistry_students)
# print(monlyonly)
# print((math_students | physics_students) - chemistry_students) # | - то же что и union

#Задача 62
mn1 = set()
mn2 = set()
mn3 = set()
for i in range(1,22):
    if i %2 == 0:
        mn1.add(i)
print(mn1)
for i in range(1,32):
    if i % 3 == 0:
        mn2.add(i)
print(mn2)
print(mn2.intersection(mn1))
for i in range(1,20):
    if i%2 == 0 and i%3 == 0:
        mn3.add(i)
print(mn3)
