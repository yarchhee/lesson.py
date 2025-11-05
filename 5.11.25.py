# nums = [1, 2, 3]
# my_iter = iter(nums)
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

# k = [1,2,3]
# k = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for i in range(0,len(k)):
#     k[i] += 1
# print(k)

# k = [1, 2, 3]
# l = [4, 5, 6]
# z = k + l
# print(z)
## k.extend(l) #расширяет один обьект другим
## print(k)

# from random import randint
# k = []
# for i in range(5):
#     #добавляет новы элемент в конец списка
#     k.append(randint(1, 100))
# print(k)

# k = ["раз","Три"]
# j = ["Два"]
# k.insert(1,j) #вставляет перед необходимым индексом значение
# print(k)

# k = [1,2,3,4,2,5]
# k.remove(3) #удаляет первый найденный элемент в списке
# print(k)

# k = [1,2,3,4,2,5]
# k.clear() #чистит список
# print(k)

# k = [1,2,3,4,2,5]
# k.pop(4) #удаляет элемент по индексу
# print(k)

# k = [5,4,3,2,1,2,3,4,5]
# k = ["alfa", "celcy", "beta", "bata", "e", "f"]
# #k.sort()
# k.sort(reverse = False)
# print(K)

# k = [1,2,3,4,5]
# k.reverse() #переворачивает список
# print(k)

# k = [1,2,3,4,5]
# print(max(k))
# print(min(k))
# print(sum(k))

# Задача 1
# a = [1,2,3,4,5,6,7,8,9]
# for i in range (len(a)):
#     a[i] *=2
# print(a)

#Задача 4
# k = [10,1,3,4,5]
# iterator = iter(k)
# summury = 0
# for _ in range(len(k)):
#     summury += next(iterator)
# print(summury)

#Задача 5
# k = [1,2,3,4,5]
# z = [6,7,8,9,10]
# for i in range (len(k)):
#     print(k[i] + z[i], end=" ")

# a = ['aeeeee','be','cee','de']
# for x in a:
#     count  = 0
#     for _ in x:
#         count += 1
#     if count %2 == 0:
#         print(x)

#Задача 11
# from random import randint
# a = randint(1,100000)
# b = 0
# for i in str(a):
#     b += 1
# for j in range(1,b):
#     print('Разряд')

# from random import randint
# for _ in str(randint(0, 100000)) :print("разряд")
