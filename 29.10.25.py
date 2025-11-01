#math - библиотека для математических вычислений
#random - библиотека для генерации псевдослучайных чисел

# import math  # импортируем модуль(как коробку)
# from math import sqrt # импортируем инструмент from math
# import math as mth # меняем название модуля и импортируем

# import math
# print(math.sqrt(25))
#
# from math import pow,sqrt
# from math import * #* - все инструменты в модуле
# print(pow(10,10))
#
# import math as mth
# print(mth.pow(10,10))

# from random import randint
# print(randint(1,10)) #от какого до какого числа сделать(включительно)

# index = randint(0,4)
# l=['a','b','c','d','e']
# print(l[index])

# from random import randint, choice
# l=['a','b','c','d','e']
# print(choice(l))

#задача 9
# x = input()
# i = len(x)//2
# print(x[i:], x[:i])

#задача 14
# x = input()
# j = x[::2]
# k = x[1::2]
# print(j + k[::-1])

#задача 15
# x=input()
# for i in range(0,len(x)):
#     print(x[i:i+3])

#задача 12
# x="шалаш, камыш, заказ, возврат, поиск, довод, спектр, комок, альянс"
# x=x.split(", ")
# for i in x:
#     if i[::-1]==i:
#         print(i, "Палиндром")

#задача 16
a=input()
alpha=""
amount=0
#уникализирует список
for i in set(a):
    count=a.count(i)
    if count>amount:
        alpha=i
        amount=count
print(alpha,amount)
print(a[::3])
maxim = 0
indexes = [0,0]
for i in set(a):
    if a.count(i) == 1:
        continue
    backward = a.rfind(i)
    forward = a.rfind(i)
    if (backward-forward) > maxim:
        maxim=backward - forward
        indexes = a[forward+1:backward]
print(indexes)











