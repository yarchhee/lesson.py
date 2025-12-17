# 1
# a,b,c = input().split()
# print("Значение переменной a:", a)
# print("Значение переменной a:", b)
# print("Значение переменной a:", c)
# 2
# a,b,c,d = input().split()
# print(int(a)+int(c),int(b)*int(d))
# 3
# a = int(input())
# b = 1
# for x in str(a):
#     b *= int(x)
# print("Произведение разрядов числа" ,a,":", b)
# 4
# a,b = map(int,input().split())
# a = a+(b*3)
# b = b+(a%b)
# print("Первое число:",a)
# print("Второе число:",b)
# 5
# a = int(input())
# if a%2 != 0:
#     print("Удвоенное число:",a*2)
# else:
#     print("Число без изменений:",a)
# 6
# a = int(input())
# if a%2 != 0 and a//100 == 0 or a//100 == 2 or a//100 == 4 or a//100 == 6 or a//100 == 8:
#     a+=1
# elif a%10 == 3 or a%10 == 7 or a%10 == 7:
#     a-=1
# print(a)
# 7
# def f(x):
#     if x > 0:
#         return 3*x + 1
#     elif x == 0:
#         return x
#     elif x < 0:
#         return x*2 + 2
# print(f(int(input())))
# 8
# a = input()
# b = int(a,16)
# c = ""
# while b > 0:
#     c+=str(b%2)
#     b = b//2
# print("Введенное число в 2 сс:", c)
# print("Количество единиц:",c.count("1"))
# 9
# a = int(input())
# d = 0
# for x in str(a):
#     d+=int(x)
# print(d)
# 10
# a,b = input().split(",")
# # # первое условие пропустил
# print(a[9:-6])
# print(a[::-3])
# 11
# a = input().split()
# b = ""
# for i in a:
#     b += i[::-1]
#     b += " "
# print(b)
# 12
# a = "a1b2, c3d4, e5f6, g7h8"
# b = a.split(", ")
# s1 = b[0]
# s2 = b[1]
# s3 = b[2]
# s4 = b[3]
# d = ""
# for i in s1:
#     if i.isnumeric():
#         d += i
# for i in s2:
#     if i.isnumeric():
#         d += i
# for i in s3:
#     if i.isnumeric():
#         d += i
# for i in s4:
#     if i.isnumeric():
#         d += i
# print("Первая строка:", s1)
# print("Вторая строка:", s2)
# print("Третья строка:", s3)
# print("Четвертая строка:", s4)
# print("Только цифры:", d)
# 13
# a = input().split()
# d = []
# flag = False
# for i in a:
#     d.append(int(i))
# for i in d:
#     if i % 2 == 0 and i % 13 == 0:
#         g = d[:d.index(i)]
#         flag = True
#         print("Cписок:", d)
#         print("Сумма элементов до числа",i,':', sum(g))
#         break
# for i in d:
#     if flag == False:
#         print("Список:", a)
#         print("Подходящих элементов не найдено")
#         break
# 14
# a = input().split()
# d = []
# c = []
# for i in a:
#     d.append(int(i))
# for i in d:
#     if i % 2!=0:
#         c.remove(i)
# print("Cписок:", d)
# print("Только четные числа:", c)
# print("Сумма всех оставшихся:", sum(c))








