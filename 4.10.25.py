#кортеж - набор неизменямых данных (tuple)
#a = (1,2,3,4,5,6,6)
#print(a, type(a))

#set - набор упорядоченных по возразастанию уникальных значений (неизменяемый)
#a = {1,2,3,4,5,5}
#print(a , type(a))

#list_1 = [1,2,2,2,3,3,3,4,4,4,5,5]
#print(set(list_1))
#{1,2,3,4,5}

#a = ["раз","два","три"]
#print(a[0],a[1],a[3], sep="-")

#задание 1
#student={"имя":"Иван", "фамилия":"Иванов",  "возраст":"17", "класс":"11А"}
#print(student["имя"],student["фамилия"],student["возраст"],student["класс"])

#задание 2
#a=45
#a=str(a)
#print("Число в строке:", a)

#задание 3
#a=str(input())
#b=str(input())
#c=str(input())
#print(a,b,c, sep=",")

#задание 6
#a=float(input())
#b=float(input())
#a=int(a)
#b=int(b)
#print(a+b)

#задача 7
#a=[input(), input(), input()]
#print(a[0],a[1],a[2], sep=":")

#ВВОДИТ ЧИСЛА ЧЕРЕЗ ПРОБЕЛ
#a=input().split(" ")
#print(a[0],a[1],a[2], sep=":")

#задача 8
text="python"
text=list(text)
print(text)

#задача 9
#my_tuple = (1,2,3,4)
#a=list(my_tuple)
#print(id(my_tuple), id(a), sep=";")
#b=tuple(a)