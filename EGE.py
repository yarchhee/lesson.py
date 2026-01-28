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
# k = 0
# from itertools import *
# for x in set(permutations('ПРОБНИК')):
#     x = "".join(x)
#     if x[0] not in "ОИ" and x[-1] not in "ОИ":
#         if "ИО" not in x and "ОИ" not in x:
#             if len(x) == 7:
#                 k+=1
# print(k)

# k = 0
# from itertools import *
# for x in set(permutations("КЛАБХАУС")):
#     s = "".join(x)
#     if all((i) * 2 not in s for i in s):
#         k = k + 1
# print(k)

# z = []
# for a in "КОНЕЦ":
#     for b in "КОНЕЦ":
#         for c in "КОНЕЦ":
#             for d in "КОНЕЦ":
#                 for e in "КОНЕЦ":
#                     s = a + b + c + d + e
#                     z.append(s)
# v = []
# for a in "ДРАКОН":
#     for b in "ДРАКОН":
#         for c in "ДРАКОН":
#             for d in "ДРАКОН":
#                 for e in "ДРАКОН":
#                     s = a + b + c + d + e
#                     v.append(s)
# b = [i for i in z if i not in v ]
# print(len(b))

# from itertools import *
# k = 0
# for x in permutations("ХОЧУНАБЮДЖЕТ"):
#     s = "".join(x)
#     if "ООООО" not in s and "УУУУУ" not in s and "ААААА" not in s and "ЮЮЮЮЮ" not in s and "ЕЕЕЕЕ" not in s:
#         k += 1
# print(k)
# k = 0
# for a in "ЭЮЯ":
#     for b in "АБВГ":
#         for c in "АБВГ":
#             for d in "АБВГ":
#                 for e in "ЭЮЯ":
#                     s = a+b+c+d+e
#                     k += 1
# print(k)
# k = 0
# for a in "АБВГДЯ":
#     for b in "АБВГДЯ":
#         for c in "АБВГДЯ":
#             for d in "АБВГДЯ":
#                 for e in "АБВГДЯ":
#                     s = a+b+c+d+e
#                     if s.count("Я") == 3 :
#                         k+=1
# print(k)
# k = 0
# for a in "КАТЕР":
#     for b in "КАТЕР":
#         for c in "КАТЕР":
#             s = a + b + c
#             if s.count("Р") >= 2:
#                 k += 1
# print(k)
# k = 0
# for a in "ДЖОБС":
#     for b in "ДЖОБС":
#         for c in "ДЖОБС":
#             for d in "ДЖОБС":
#                 for e in "ДЖОБС":
#                     for f in "ДЖОБС":
#                         s = a+b+c+d+e + f
#                         if s.count("Д") == 1 and s.count("О") == 1 and s.count("С") == 1 and s.count("Ж") <= 2:
#                             k+=1
# print(k)

# k = 0
# for a in "1234567":
#     for b in "01234567":
#         for c in "01234567":
#             for d in "01234567":
#                 for e in "01234567":
#                     s = a + b + c + d + e
#                     if s.count("6") == 1 and "16" not in s and "61" not in s and "36" not in s and "63" not in s and "56" not in s and "65" not in s and "76" not in s and "67" not in s :
#                         k+=1
# print(k)
# def fun(n):
#     for i in range(len(n) - 1):
#         if (int(n[i]) + int(n[i + 1])) %2 == 0:
#             return False
#     return True
# k = 0
# for a in "123456":
#     for b in "0123456":
#         for c in "0123456":
#             for d in "0123456":
#                 for e in "0123456":
#                     for f in "0123456":
#                         s = a+b+c+d+e+f
#                         if s.count("6") == 1 and fun(s):
#                             k += 1
#
# print(k)\
# k =0
# for a in "ABCD":
#     for b in "ABCD":
#         for c in "ABCD":
#             for d in "ABCD":
#                 s = a + b + c + d
#                 if s[0] <= s[1] <= s[2] <= s[3]:
#                     k+=1
# print(k)

# k = 0
# for a in "ЧОАНИМЕ":
#     for b in "ЧОАНИМЕ":
#         for c in "ЧОАНИМЕ":
#             for d in "ЧОАНИМЕ":
#                 s = a+b+c+d
#                 if s.count("М") == 3:
#                     k+=1
# for a in "ЧОАНИМЕ":
#     for b in "ЧОАНИМЕ":
#         for c in "ЧОАНИМЕ":
#             for d in "ЧОАНИМЕ":
#                 for e in "ЧОАНИМЕ":
#                     s = a+b+c+d+e
#                     if s.count("М") == 3:
#                         k+=1
# for a in "ЧОАНИМЕ":
#     for b in "ЧОАНИМЕ":
#         for c in "ЧОАНИМЕ":
#             for d in "ЧОАНИМЕ":
#                 for e in "ЧОАНИМЕ":
#                     for f in "ЧОАНИМЕ":
#                         s = a+b+c+d+e+f
#                         if s.count("М") == 3:
#                             k+=1
# print(k)
# k = 0
# from itertools import *
# for x in product("012345678", repeat = 7 ):
#     s = "".join(x)
#     if s[0] != "0" and s[0] != "3" and s[0] != "7":
#         if "00" not in s and "11" not in s and "22" not in s and "33" not in s and "44" not in s and "55" not in s and "66" not in s and "77" not in s and "88" not in s:
#             k+=1
# print(k)
# k = 0
# from itertools import *
# for x in product("ГЕПАРД", repeat = 5):
#     s = "".join(x)
#     if s.count("Г") == 1 and s[0] != "А" and s[-1] != "Е":
#         k+=1
# print(k)
# k = 0
# for a in "АРБУЗ":
#     for b in "АРБУЗ":
#         for c in "АРБУЗ":
#             for d in "АРБУЗ":
#                 for e in "АРБУЗ":
#                     for f in "АРБУЗ":
#                         s = a+b+c+d+e+f
#                         if s.count("А") == 3:
#                             if "ААА" not in s and "АА" in s:
#                                 k+=1
# print(k)
# k = 0
# from itertools import *
# for x in product("ПОЛИНА",repeat=8):
#     s = "".join(x)
#     if s.count("П") + s.count("Л") + s.count("Н") > s.count("О") + s.count("И") + s.count("А"):
#         k+=1
# print(k)
# k = 0
# for a in "КАЛИ":
#     for b in "КАЛИЙ":
#         for c in "КАЛИЙ":
#             for d in "КАЛИЙ":
#                 for e in "КАЛИЙ":
#                     s = a+b+c+d+e
#                     if s.count("К") == 1 and s.count("А") == 1 and s.count("Л") == 1 and s.count("И") == 1 and s.count("Й") == 1:
#                         if "ИА" not in s:
#                             k+=1
# print(k)
# k = 0
# for a in "КОМЕТА":
#     for b in "КОМЕТА":
#         for c in "КОМЕТА":
#             for d in "КОМЕТА":
#                 for e in "КОМЕТА":
#                     for f in "КОМЕТА":
#                         s = a+b+c+d+e+f
#                         if s.count("К") == 1 and s.count("О") == 1 and s.count("М") == 1 and s.count("Е") == 1 and s.count("Т") == 1 and s.count("А") == 1:
#                             if "ОО" not in s and "ОЕ" not in s and "ОА" not in s and "ЕО" not in s and "ЕЕ" not in s and "ЕА" not in s and "АО" not in s and "АЕ" not in s and "АА" not in s:
#                                 if "КК" not in s and "КМ" not in s and "КТ" not in s and "МК" not in s and "ММ" not in s and "МТ" not in s and "ТК" not in s and "ТМ" not in s and "ТТ" not in s:
#                                     k +=1
# print(k)
# k = 0
# from itertools import *
# for x in set(permutations("ОДЕКОЛОН")):
#     s = "".join(x)
#     if all((i)*2 not in s for i in s):
#         k+=1
# print(k)
# k = 0
# for a in "АЕЛРСТ":
#     for b in "АЕЛРСТ":
#         for c in "АЕЛРСТ":
#             for d in "АЕЛРСТ":
#                 for e in "АЕЛРСТ":
#                     s = a+b+c+d+e
#                     k+=1
#                     if s[0] not in "АСТ" and s.count("Л") == 2:
#                         if "ЛЛ" not in s:
#                             if k%2 == 0:
#                                 print(k)
# k = 0
# for line in open("9.txt"):
#     a = list(map(int, line.split()))
#     a1 = [i for i in a if a.count(i) == 3]
#     an = [i for i in a if a.count(i) == 1]
#     k += 1
#     if len(a1) == 3 and len(an) == 4:
#         if sum(a1) < sum (an):
#
#             print(k)

# from math import *
# n = 10 + 70
# for leng in range (1, 100000):
#     bit = ceil(log2(n))
#     bytenaslovo = ceil(bit / 8 * leng)
#     if bytenaslovo * 1234567 > 24 * 1024 * 1024:
#         print(leng)
#         break

# a = 51
# s = []
# k = 0
# while a>0:
#     s.append(a%2)
#     a = a//2
# for i in s:
#     if i>8:
#         k+=1
# print(s)




