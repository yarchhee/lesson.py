# for i in range(10):
#     print(i)
#
#  for i in range (30):
#      print(i)


# значения принимаемые функцией
# def name_func(first_arg = 10,*, second_arg = 15): #функция
#     #тело функци
#     for i in range(first_arg, second_arg):
#         print(i)
#     #конец тела функции
# #названя функций уникальны (строятся как переменные)
# def name_func_2(x,y, /):
#     print(x,y)
#     pass #ничего(заглушка)
# #параметры
# # name_func(10, second_arg = 25)# вызов функции
# # name_func(second_arg = 25)
# # name_func(first_arg = 5, second_arg = 25)
# name_func_2(2, 5)
# # name_func_2(2,5)

# def name_func_3(*args):
#     for i in args:
#         print(i)
# name_func_3(1,2,3,'hello',4,5)

#словарь - kwargs
# def name_func_4(**kwargs):
#     kwargs.pop('name2')
#     print(kwargs)
#
# name_func_4(name1 = 1000, name2 = 2)

# def a():
#     def b(x):
#         print(x + "world")
#     b("hello")
# a()
#
# x = 20 #глобальная область видимости
# def local_func():
#     # global x
#     x = 10 #локальная область видимости
#     print(x)
#
#     return x,x,x #возвращаем значение
#
# print(local_func()[0] + 25)
# print(x)

# def a():
#     x = 10 #охватывающая область
#     def b():
#         nonlocal x
#         x = 5
#         print(x)
#     b()
#     print(x)
# a()

# def square(x):
#     while True:
#         while True:
#             if x == 5:
#                 return
#             x +=1
#
# print(square(10))
# x:int = 0
# def func(s;str) -> list:
#     """
#     многострочные комментарии
#     можно так сделать
#     """
#     global x
#     while True:
#         while True:
#             if x >=5:
#                 return [1,2,3]
#             x+=1
# func()
# print(x)

#Задача 2
# def func(arg_1, arg_2):
#     if type(arg_1) == int and type(arg_2) == int and arg_2 !=0:
#         return arg_1 / arg_2
#     return 0

# type(x) == int --> isinstance(x, int)

#Задача 3
# def is_even(n):
#     return n % 2 == 0
# print(is_even(int(input())))

# Напишите функцию, которая принимает
# в качестве аргументов 2 четырёхзначных числа
# и возвращает кортеж произведений соответствующих разрядов этих чисел.
def a(arg_1, arg_2):
    for i,j in arg_1, arg_2:
        print(i, j)
print(a(int(input()),int(input())))

