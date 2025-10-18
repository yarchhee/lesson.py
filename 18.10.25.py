# задача 15
# a=int(input())
# b=False
# for i in range(2,a):
#     if a%i==0:
#         b=True
#         print("Составное")
#         break
# if b==False:
#     print("Простое")

# Task 18
a = int(input())
b = False
for i in range(a-1,0,-1):
    if i%3==0:
        print(i)
        b = True
        break
if b==False:
    print("Таких чисел нет")

# Задача 20
a=input()
#in - в условиях проверяет принадлежность
b="aeiouyAEIOUY"
for i in a:
    if i not in b:
        print(i, end="")#end - устанавливаем свой символ в конце по умолчанию \n

#Задача 24
for i in range(3,-1,-1):
    print("*" * (4-i) + " "*i)
for i in range(3,0,-1):
    print("*" * i + " "*(4-i))
    #ИЛИ
for i in range(1,8):
    if i>4:
        print("*"*(8-i))
        continue
    print("*"*i)



