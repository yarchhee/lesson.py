# - в строке одно число повторяется трижды, остальные числа различны;
# - максимальное число строки не повторяется.
# В ответе запишите только число.
# k = 0
# for line in open("9"):
#     a = sorted(list(map(int, line.split())))
#     a3 = [x for x in a if a.count(x)==3]
#     a1 = [x for x in a if a.count(x)==1]
#     if len(a3) == 3 and len(a1) == 4    :
#         if a.count(a[-1]) == 1:
#             k+=1
# print(k)

# Откройте файл электронной таблицы, содержащей в
# каждой строке шесть натуральных чисел. Определите сумму
# номеров строк таблицы, для чисел которых выполнены оба условия:
# – в строке все числа различны;
# – куб разности наибольшего и наименьшего чисел не меньше квадрата суммы четырёх оставшихся.
# sumi = 0
# stroka = 0
# for line in open("9"):
#     a = sorted(list(map(int, line.split())))
#     stroka  += 1
#     if len(set(a)) == 6 and (a[-1] - a[0])**3 >= sum(a[1:-1])**2:
#         sumi += stroka
# print(sumi)


# Определите количество строк таблицы, для чисел которых выполнены все условия:
# • в строке есть одно число, которое повторяется ровно 3 раза;
# • повторяющееся число нечетно;
# • неповторяющееся число четно.
# • В ответе запишите только число
# k = 0
# for line in open('9.txt'):
#     a = list(map(int, line.split()))
#     a3 = [x for x in a if a.count(x) == 3]
#     a1 = [x for x in a if a.count(x) == 1]
#     if len(a3) == 3 and a3[0] %2 != 0 and a1[0] % 2 == 0:
#         k+=1
# print(k)


# Среди шести чисел есть повторяющиеся (как ёлочные игрушки одного вида в коробке).
# • Максимальное число в строке встречается только один раз (оно — уникальное, как
# главная звезда на вершине ёлки).
# • Сумма всех повторяющихся чисел (каждое учитывается столько раз, сколько оно
# встречается) строго меньше максимального числа в этой строке (как будто суммарная
# «сила» повторов ещё не достаточна, чтобы активировать полное заклинание). Ваша задача
# — помочь аналитикам подсчитать количество таких строк.
# k = 0
# for line in open("9.txt"):
#     a = sorted(list(map(int, line.split())))
#     ap = [x for x in a if a.count(x)>1]
#     if len(ap)>1 and a.count(a[-1]) == 1 and sum(ap)<a[-1]:
#         k += 1
# print(k)
# При регистрации в компьютерной системе каждому пользователю выдаётся пароль,
# состоящий из 10 символов и содержащий только символы из 26-символьного латинского алфавита.
# В базе данных для хранения сведений о каждом пользователе отведено одинаковое и минимально
# возможное целое число байт. При этом используют посимвольное кодирование паролей, все символы
# кодируют одинаковым и минимально возможным количеством бит. Кроме собственно пароля, для каждого
# пользователя в системе хранятся дополнительные сведения, для чего отведено 6 байт на одного пользователя.
# Определите объём памяти (в байтах), необходимый для хранения сведений о 30 пользователях.
# from math import *
# n = 26
# bit = ceil(log2(n))
# byte = ceil(bit/8 * 10)
# password = (byte + 6) * 30
# print(password)
# k = 0
# for a in "WXYZ":
#     for b in "ABC":
#         for c in "ABC":
#             for d in "ABC":
#                 for e in "ABC":
#                     for f in "WXYZ":

# k = 0
# for a in "ГЕПРД":
#     for b in "ГЕПАРД":
#         for c in "ГЕПАРД":
#             for d in "ГЕПАРД":
#                 for e in "ГПАРД":
#                     s = a+b+c+d+e
#                     if s.count("Г") == 1:
#                         k+=1
# print(k)

# k = 0
# for a in "АБИКОЛУН":
#     for b in "АБИКОЛУН":
#         for c in "АБИКОЛУН":
#             for d in "АБИКОЛУН":
#                 for e in "АБИКОЛУН":
#                     for f in "АБИКОЛУН":
#                         for g in "АБИКОЛУН":
#                             for h in "АБИКОЛУН":
#                                 s = a+b+c+d+e+f+g+h
#                                 if s.count("А") == 1 and s.count("Б") == 1 and s.count("И") == 1 and s.count("К") == 1 and s.count("О") == 1 and s.count("Л") == 1 and s.count("У") == 1 and s.count("Н") == 1:
#                                     if "АО" not in s and "АИ" not in s and "АУ" not in s and "ИА" not in s and "ИО" not in s and "ИУ" not in s and "ОА" not in s and "ОИ" not in s and "ОУ" not in s and "УА" not in s and "УИ" not in s and "УО" not in s:
#                                         if "БК" not in s and "БЛ" not in s and "БН" not in s and "КБ" not in s and "КЛ" not in s and "КН" not in s and "ЛБ" not in s and "ЛК" not in s and "ЛН" not in s and "НЛ" not in s and "НБ" not in s and "НК" not in s:
#                                             k+=1
# print(k)

# k = 0
# for a in "012345678":
#     for b in "012345678":
#         for c in "012345678":
#             for d in "012345678":
#                 for e in "012345678":
#                     for f in "012345678":
#                         for g in "012345678":
#                             s = a+b+c+d+e+f+g
#                             if s.count("8") == 1 and s[0] not in "01357" and s[-1] not in "02468":
#                                 k+=1
# print(k)

# Определите количество шестизначных чисел, записанных в семеричной системе счисления, в записи которых
# ровно одна цифра 6, при этом чётные и нечётные цифры чередуются.
# k = 0
# def fun(n):
#     for i in range(len(n) - 1):
#         if (int(n[i]) + int(n[i+1])) %2 == 0:
#             return False
#     return True

# for a in "123456":
#     for b in "0123456":
#         for c in "0123456":
#             for d in "0123456":
#                 for e in "0123456":
#                     for f in "0123456":
#                         s = list(a+b+c+d+e+f)
#                         if s.count("6") == 1 and fun(s):
#                             k+=1
#
# print(k)

# def fun(n):
#     for i in n:
#         if i == "Ь":
#             if n.index(i) :
#
#
#
# for a in "АПЕЛЬСИН":
#     for b in "АПЕЛЬСИН":
#         for c in "АПЕЛЬСИН":
#             for d in "АПЕЛЬСИН":
#                 for e in "АПЕЛЬСИН":
#                     for f in "АПЕЛЬСИН":
#                         for g in "АПЕЛЬСИН":
#                             s = a+b+c+d+e+f+g

# from itertools import *
# k = 0
# for x in set(permutations("ЗАПИСЬ")):
#     s = "".join(x)
#     if s[0] != "Ь" and "ИЬ" not in s and "АЬ" not in s:
#         k += 1
# print(k)

# k = 0
# for a in "ВАФУ":
#     for b in "ВАЙФУ":
#         for c in "ВАЙФУ":
#             for d in "ВАЙФУ":
#                 s = a+b+c+d
#                 if "ВФ" not in s and "ФВ" not in s and s.count(s[0]) == 1 and s.count(s[1]) == 1 and s.count(s[2]) == 1 and s.count(s[3]) == 1:
#                     k+=1
# print(k)
# k = 0
# for a in "ПИКАЧУ":
#     for b in "ПИКАЧУ":
#         for c in "ПИКАЧУ":
#             for d in "ПИКАЧУ":
#                 for e in "ПИКАЧУ":
#                     s = a+b+c+d+e
#                     if s.count("У") >= 2:
#                         k+=1
# print(k)
# k = 0
#
# for a in "СОТКАПЛЗ":
#     for b in "СОТКАПЛЗ":
#         for c in "СОТКАПЛЗ":
#             for d in "СОТКАПЛЗ":
#                 for e in "СТКПЛЗ":
#                     s = a+b+c+d+e
#                     if "ЗЛО" not in s :
#                         if s.count(s[0]) == 1 and s.count(s[1]) == 1 and s.count(s[2]) == 1 and s.count(s[3]) == 1 and s.count(s[4]) == 1:
#                             k+=1
# print(k)
# k = 0
# for a in "013578":
#     for b in "012345678":
#         for c in "012345678":
#             for d in "012345678":
#                 for e in "012345678":
#                     for f in "012345678":
#                         for g in "012345678":
#                             s = a+b+c+d+e+f+g
#
# print(k)
