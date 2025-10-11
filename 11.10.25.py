#Задача 5
# a=int(input())
# if a%4==0 and a%100 !=0 and a%400==0:
#     print("YES")

#Задача 13
# a=int(input())
# if a ==1:
#     b=int(input())
#     print(3.14*b**2)
# elif a == 2:
#     c=int(input())
#     d=int(input())
#     print(c*d*3.14)
# else:
#     print("NO")

#Задача 15
# a=int(input())
# a1=a%10
# a2=a//100
# a3=a//10%10
# count=0
# if a1 % 2 == 0 or a1 % 5 == 0:
#     count+=1
# if a2 % 2 == 0 or a2 % 5 == 0:
#     count+=1
# if a3 % 2 == 0 or a3 % 5 == 0:
#     count+=1
# if count>=2:
#     print(a)
# else:
#     print(a+1)

#Задача 17
# a=int(input())
# b=int(input())
# c=int(input())
# if a >= (b+c) and b >= (a+c) and c >= (a+b):
#      print("NET")
# elif a==b==c:
#     print("Равносторонний")
# elif a==b or a==c or b==c:
#     print("Равнобедренный")
# elif a!=b and a!=c and b!=c:
#     print("Разосторонний")

#Задача 20
a=int(input())
match a:
    case 1:
        print("31")
    case 2:
        print("28")
    case 3:
        print("31")
    case 4:
        print("30")
    case 5:
        print("31")
    case 6:
        print("30")
    case 7:
        print("31")
    case 8:
        print("30")
    case 9:
        print("31")
    case 10:
        print("30")
    case 11:
        print("31")
    case 12:
        print("30")
    case _:
        print("Нет такого месяца")

#Задача 22
a=str(input())
b=int(input())
match (a,b):
    case ("Рабочий", t) if 9<=t<=18:
        print("Рабочее время")
    case("Выходной", c) if 10<=c<=16:
        print("Work time")
    case("Праздничный", b):
        print("Не работает")
    case _:
        print("error")

