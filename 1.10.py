#Переменная - именованная ячейка в памяти
user_name = "Алиса" #строковый тип - String(str)
max_value = 100 #Численный тип - integer(int)
our_float = 1.6 #число с плавающей точкой float(float)
logical = True #True/False (1 или 0)- boolean (bool)

#id() - возвращает адрес в памяти
print(id(user_name), max_value, our_float, logical)

a = 2
b = 2
a = b
print( id(a), id(b) )

#определяет тип переменной (обьекта)
#a = 4 #выведет int
#print(type(a))

a = int(1) #переводит в int
print(type(a), a)
a = float(a) #переводит в float
print(type(a),a)
a = str(a) #переводит в строку
print(type(a),a)
a = bool(a) #переводит в bool (логический тип)
print(type(a),a)

# Задача 1
x = "name"
print(x)

#Задача 2
age = 15
print("Мне", age, "лет")

a = "Текст"
# a - имя, a[index: int]
#index начинается с 0
#index целое число
print(a[0]) #Синтаксис получения элемента по индексу

my_list = [1, 2, "Hello", 4, 5] #тип данных (list)
print(my_list[2]) #выведет Hello
print(my_list[2].__sizeof__()) #показывает размер в битах

my_list = [1,2,3,4,5,6,7,8,9,10] #always list(в питоне нет массивов)
# * / + - (базовые операторы)
print(my_list[1] / 3 - 2)

#{} - dict(словарь) в качестве аргумемнтов ключь : значение
dictonary = {"a":10}
print(dictonary["a"])

#input - команда ввода данных
a = input("Введите текст: ")
print("Вы ввели:", a)
a = int(input("Введите текст: "))
print(a*10)

a=int(input())
b=int(input())
print(a+b)

