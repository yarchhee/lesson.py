#задача 28
# a = input()
# print(a.islower())
# print(a.isupper())
# print(a.istitle())
#задача 30
# a = input()
# if not(a.isalpha()):
#     print(a.upper())
# if not(a.isdigit()):
#     print(a.replace(' ','*'))
# else:
#     print(a)

#задача 32
# j = input()
# a = "аеёиоуыэюя"
# maxim = 0
# alpha = ""
# for i in a:
#     new_maxim = j.rfind(i)
#     if maxim < new_maxim:
#         maxim = new_maxim
#         alpha = i
# print(maxim,alpha)

#задача 31
# s="abcd defg ghij"
# s=s.replace(" ", "")
# for i in s:
#     if s.count(i)>1:
#         s=s.replace(i,"")
# print(s)

#задача 20
# from random import choice
#                            #choice-случайный эл-т последовательности
# s=input()
# k=[" ",",",".","!","?"]
# while s:
#     a=choice(s)
#     if a in k:
#         continue
#     s=s.replace(a, "")
#     print("Удаляем букву", a, ":", s)

#задача 19
a=input()
k="АВЕКМНОРСТУХ"
if len(a) == 6:
    numbers = a[1:4]
    alpha = a[:1] + a[4:]
    print(numbers.isnumeric() and alpha[0] in k and alpha[1] in k and alpha[2] in k )
else:
    print(False)




