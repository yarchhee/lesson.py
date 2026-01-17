
# lambda аргументы: тело функции (выражение)
# square = lambda x: print(x)

numbers = [-1, 2, -3, 4, 5]
# def double_pos(num):
#     if num>0:
#         return num*2
#     return num
#
# pos_doubled = [double_pos(i) for i in numbers]

# pos_double = lambda num: num *2 if num > 0 else num
# pos_doubled = [pos_double(i) for i in numbers]
# print(pos_doubled)
# pos_doubled = list((lambda num: num*2 if num>0 else num(number for number in numbers)))
# dict_students = [
#     {"name" : "john", "age" : 25, 'grade' : 10},
#     {"name" : "Борис", "age" : 10, 'grade' : 1},
#     {"name" : "Аркадий", "age" : 30, 'grade': 4}
# ]
# get_name = lambda student: student.get('name')
# get_age = lambda student: student.get('age')
# get_grade = lambda student: student.get('grade')
# names = [get_name(student) for student in dict_students]
# ages = [get_age(student) for student in dict_students]
# grades = [get_grade(student) for student in dict_students]
# print(names)
# print(ages)
# print(grades)

# unsorted_list = [4,3,2,5,1]

# unsorted_dict = {
#     4 : "Мария"
#     2 : "Иван"
#     1 : "Алиса"
#     3 : "Павел"
# }
# print(sorted(unsorted_list))

# words = ["hello", "my", "name"]
# sorted_list = sorted(words, key = len)
# print(sorted_list)

# nums = [14,5,23,42,31]
# sorted_nums = sorted(nums, key=lambda x: x%10)
# print(sorted_nums)

# students = [
#     ("John", 98),
#     ("Michael", 77),
#     ("Bob", 92),
#     ("Robert", 84),
#     ("Kevin", 85)
# ]
# print(sorted(students, key = lambda x: x[1]))

# dict_students = [
#     {"name" : "john", "age" : 25, 'score' : 98},
#     {"name" : "Борис", "age" : 10, 'score' : 77},
#     {"name" : "Аркадий", "age" : 30, 'score': 92},
#     {"name" : "HelloKitty", "age" : 30, 'score': 84},
#     {"name" : "АркадийПаровозов", "age" : 30, 'score': 85}
# ]
# a =sorted(dict_students, key = lambda student: student['score'])
# print(a[::-1])

# students= [
#     ("Алиса", 4),
#     ("Борис", 5),
#     ("Виктор", 4),
#     ("Галина", 3),
#     ("Дмитрий", 5),
#     ("Елена", 3)
# ]
# students_sorted = sorted(students, key=lambda student: student[1], reverse=True)
# for name, grade in students_sorted:
#     print(f'{name}:оценка {grade}')
# a = input()
# str_len = lambda x: len(x)*8
# print(str_len(a))

# is_even = lambda x: x % 2 == 0
# print(is_even(4))

# Создайте обычную функцию my_logger(),
# которая принимает лямбда-функцию и целое число.
# Эта функция должны выводить следующее сообщение:
# undefined Пользователь применяет свою функцию.
# Передано число: {num}.
# Результат: {result}
# Создайте лямбда-функцию для возведения числа в третью степень и передайте ее в функцию my_logger() вместе с числом 5.
# def my_logger(func, num):
#     print(f'Передано число:{num}.\n'
#           f'Результат : {func(num)}')
# my_logger(lambda x: x**3, 5)

data = [(1,"b"),(3,"a"),(2,"c")]
print(sorted(data, key = lambda x: x[1]))



