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
from itertools import permutations


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
# k = 0
#
# from itertools import *
# for x in set(permutations("СОРТИРОВКА")):
#     s = "".join(x)
#     for i  in "ОИА":
#         s = s.replace(i, "А")
#     for io in "СРТВК":
#         s = s.replace(io, "Б")
#     if "ААА" not in s and "БББ" not in s:
#         k = k + 1
# print(k)
# k = 0
# from itertools import *
# for x in product(sorted("МИНУС"), repeat = 4):
#     s = "".join(x)
#     k+=1
#     gl = [i for i in s if i in "ИУ"]
#     sogl = [i for i in s if i in "МНС"]
#     # for i in s:
#     #     if i in "ИУ":
#     #         s = s.replace(i, "Г")
#     #     if i in "МНС":
#     #         s = s.replace(i, "С")
#     if len(gl)<=len(sogl):
#         print(k)

# from itertools import *
# def vow_more_cons(word):
#     vow = "ИУ"
#     cons = "МНС"
#     # Считаем количество гласных
#     vcount = 0
#     for char in word:
#         if char in vow:
#             vcount += 1
#
#     # Считаем количество согласных
#     ccount = 0
#     for char in word:
#         if char in cons:
#             ccount += 1
#
#     # Возвращаем True, если гласных больше, иначе False
#     return ccount >= vcount
#
# answers=[]
# k=0
# for x in product(sorted('МИНУС'),repeat=4):
#     s=''.join(x)
#     k=k+1
#     if (vow_more_cons(s)==True):
#         answers.append(k)
#         print(k,s)
#     # print(s)
# print(max(answers))
# k = 0
# counter = 0
# from itertools import *
# for x in product(sorted("СОЛНЦЕ"), repeat = 6):
#     s = "".join(x)
#     k += 1
#     if k%2 == 0:
#         if s[0] not in "ОЕ" and s.count("Ц") == 2:
#             counter += 1
# print(counter)

# k = 0
# for line in open('999'):
#     k+=1
#     a = list(map(int, line.split()))
#     a4 = [i for i in a if a.count(i) == 4]
#     an = [i for i in a if a.count(i) == 1]
#     if len(a4) == 4 and len(an) == 3:
#         if sum(an) < sum(a4):
#             print(k)
#
# print("x y z w F")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = int(w and (( y<=x ) <= z))
#                 print(x, y, z, w, F)

# x y z w F
# 0 0 1 1 1
# 0 1 0 1 1
# 0 1 1 0 0
# 0 1 1 1 1
# 1 0 0 1 0
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 0 0 0
# 1 1 0 1 0
# 1 1 1 0 0

# from itertools import *
# def f(x,y,z,w):
#     return ((x == y) and (z and (not(w)))) == (not(((y<=w)and(z==y))or y))
# for a,b,c,d in product([1,0], repeat = 4):
#     table = [(1,a,0,1),
#              (1,b,1,1),
#              (0,1,c,1),
#              (1,1,d,1),]
#     if len(table) == len(set(table)):
#         for p in permutations("xyzw", r = 4):
#             if [f(**dict(zip(p,r)))for r in table] == [0,0,0,0]:
#                 print(p)


# x y z w
# 0 1 1 0 0
# 0 1 1 1 0

# 1 1 0 1 0

# from itertools import *
# def f(x,y,w,z):
#     return (z == (not(x))) <= ((w <= (not(y))) and (y <= x))
# for a1,a2,a3,a4, a5 in product([0,1], repeat=4):
#     table = [(1,1,1,0), (a1,a2,0,0), (a3,0,a4,a5)
#     if len(set(table))==3:
#         for p in permutations('xywz'):
#             if [f(**dict(zip(p,r))) for r in table]==[1,0,0]:
#                 print(p)

# a b c t
# 0 0 1 1 1
# 0 1 0 0 0
# 0 1 0 1 1
# 0 1 1 0 0
# 0 1 1 1 1

# w x y z
# 0 0 1 0 1
# 0 0 1 1 0
# 0 1 0 1 0
# 0 1 1 0 0
# 0 1 1 1 0
# 1 0 0 0 0
# 1 0 0 1 0
# 1 0 1 0 1
# 1 0 1 1 1
# 1 1 0 0 0
# 1 1 0 1 0
# 1 1 1 0 0

# for a in "12345678":
#     for b in "0123456789":
#         for c in "0123456789":
#             for d in "0123456789":
#                 for e in "0123456789":
#                     for f in "0123456789":
#                         for g in "0123456789":
#                             for h in "0123456789":
#                                 for i in "0123456789":
#                                     s = a+b+c+d+e+f+g+h+i
#                                     for i in s:
#                                         d = ""
#
# k = 0
# for line in open("999"):
#     a = list(map(int, line.split()))
#     a2 = [i for i in a if a.count(i) == 2]
#     an = [i for i in a if a.count(i) == 1]
#     if len(a2) == 2 and len(an) == 3:
#         k+=1
# print(k)
# from math import *
# n = 25 + 487
# for leng in range(1,10000):
#     bit = ceil(log2(n))
#     byteslovo = ceil(bit / 8 * leng)
#     if 345 * byteslovo > 70 * 1024:
#         print(leng)
#         break


# def f(x,y,z,w):
#     return (z<=w) and y and (not(x))
# from itertools import *
# for a,b,c,d,e in product([0,1], repeat = 5):
#     table = [(0,1,a,0),(b,0,c,d),(0,1,1,e)]
#     if len(set(table)) == len(table):
#         for p in permutations("xyzw"):
#             if [f(**dict(zip(p,r))) for r in table] == [1,1,0]:
#                 print(p)



# def f(x,y,z,w):
#     return (x or(y and (not(z)))) and (not(w))
#
# from itertools import *
# table = [(1,0,0,0),(0,0,1,0),(0,1,0,1)]
# if len(set(table)) == len(table):
#     for p in permutations("xyzw"):
#         if [f(**dict(zip(p,r))) for r in table] == [1,1,0]:
#             print(p)


# def f(x,y,z,w):
#     return (y <= (x or z)) and (z<=y)
# from itertools import *
# table = [(1,0,0,0),(1,1,0,0),(1,1,0,1),(0,1,1,0)]
# if len(set(table)) == len(table):
#     for p in permutations("xyzw"):
#         if [f(**dict(zip(p,r)))for r in table] == [0,0,0,0]:
#             print(p)


# def f(w,x,y,z):
#     return x and ((w<=y)==z)
# from itertools import *
# for a,b,c,d,e in product([0,1], repeat=5):
#     table = [(a,b,0,0),(0,c,d,0),(e,1,1,1)]
#     if len(set(table)) == len(table):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p,r))) for r in table] == [1,1,0]:
#                 print(p)

# k = 0
# from itertools import *
# for x in product(range(12), repeat = 7):
#     if x.count(11) == 2 and all(x[i]%2 != x[i+1]%2 for i in range(6)):
#         k+= x [0] > 0
# print(k)
# k = 0
# for line in open('999'):
#     a = sorted(list(map(int, line.split())))
#     as5 = [i for i in a if i%10==5]
#     if (2 * (a[-1] + a[-2])) > (3 * (sum(a[:3]))):
#         if len(as5) >= 2:
#             k = k + 1
# print(k)
# from math import *
# n = 10 + 22
# bit = ceil(log2(n))
# byteslovo = ceil(bit / 8 * 15)
# for I in range(1,10000):
#     if (byteslovo * 30 <= I):
#         print(I)
#         break


# a = 2**103 + 4**98 - 8**20
# s = []
# while a>0:
#     s.append(a%8)
#     a = a//8
# print(s.count(7))

#
# def f(x,y,z,w):
#     return w and ((x<=y) == (y<=z))
#
# from itertools import *
# for x1,x2,x3,x4,x5,x6 in product([0,1],repeat=6):
#     table = [(0,x1,x2,x3),(0,0,x4,0),(0,x5,x6,0)]
#     if len(set(table)) == len(table):
#         for p in permutations("xyzw"):
#             if [f(**dict(zip(p,r))) for r in table] == [1,1,1]:
#                 print(p)
# k = 0
# from itertools import *
# for x in product("АЗИМНОПРТ", repeat = 5):
#     s = "".join(x)
#     k+=1
#     if k%2 == 0:
#         if s[0] == "Н" and s.count("Р") == 2:
#             print(k,s)
# k

# print(sum([86, 87, 93, 86, 93, 90, 91]))
# from math import *
# n = 10 + 1020
# bit = ceil(log2(n))
# byte = ceil(115 * bit / 8)
# for i in range(1,10000000):
#     if 16384 * byte <= i:
#         print(i)
#         break

# for x in range(1,3001):
#     a = 9**150 + 9**30 - x
#     s = []
#     while a > 0:
#         s.append(a%9)
#         a = a // 9
#     if s.count(0) == 122:
#         print(x)
#         break


# def f(a,b,c,d):
#     return ((a<=b) and (c<=d) or (not (c)))
# table = [(1,0,1,0),(0,0,1,1),(0,1,1,1),(1,0,1,1)]
# for p in permutations("abcd"):
#     if [f(**dict(zip(p,r)))for r in table] == [0,0,0,0]:
#         print(p)
# k = 0
# from itertools import *
# for a in set(permutations("МАКАКА")):
#     ok = True
#     for i in range(len(a)-1):
#         if a[i] == a[i+1]:
#             ok = False
#             break
#         if ok:
#             k = k + 1
# print(k)
#
# from itertools import permutations
#
# k = 0
#
# for a in set(permutations("МАКАКА")):
#     ok = True
#     for i in range(len(a) - 1):
#         if a[i] == a[i+1]:
#             ok = False
#             break
#     if ok:
#         k += 1
#
# print(k)

# n = 10 + 1550
# from math import *
# bit = ceil(log2(n))
# byte = ceil(bit * 196 / 8)
# print(byte * 65536)
# print(17694720 / 1024)

# from itertools import *
# def f(x,y,z,w):
#     return (not(((x==(not(z))) and (y<=w))<=x))
# for x1,x2,x3,x4,x5,x6,x7 in product([0,1], repeat=7):
#     table = [(x1,0,x2,0),(x3,1,0,x4),(x5,x6,1,x7)]
#     if len(table) == len(set(table)):
#         for p in permutations("xyzw"):
#             if [f(**dict(zip(p,r)))for r in table] == [1,1,1]:
#                 print(p)

# k = 0
# from itertools import *
# for s in product("АВКМОС", repeat = 6 ):
#     a = "".join(s)
#     k+=1
#     if k%2 ==0:
#         if a[0] not in "АВК":
#             if a.count('К') == 2 and 'КК' not in a:
#                 print(k, a)
#                 break
# k = 0
# for line in open("999"):
#     k+=1
#     a = list(map(int, line.split()))
#     a1 = [i for i in a if a.count(i) == 2]
#     an = [i for i in a if a.count(i) == 1]
#     ar = set(a1)
#     if len(a1) == 4 and len(an) == 2:
#         if sum(an) <= sum(ar):
#             print(sum(a))


# from math import *
# for i in range(1,100000):
#     bit = ceil(log2(i))
#     byteslovo = ceil(bit / 8 * 23)
#     if 3222444 * byteslovo >= 45 * 1024 * 1024:
#         print(i)
#         break

# a = 5*512**1000 + 256**1001 - 128**1002 + 64**1003 - 7*32**1004 - 5120
# z = []
# k = 0
# while a>0:
#     if a%32 <=9:
#         k+=1
#     a = a//32
# print(k)

# from math import *
# Ln=23
# for a in range (1,99999):
#     i=ceil(log2(a))
#     idn=ceil(i*Ln/8)
#     if 3222444*idn>=(45*1024*1024):
#         print(a)
#         break
# from itertools import *
# def f(x,y,z,w):
#     return (((w<=y) <= (x == y)) or (not(z)))
# for x1,x2,x3,x4,x5 in product([0,1],repeat=5):
#     table = [(x1,0,1,0),(0,x2,x3,0),(x4,1,1,x5)]
#     if len(table) == len(set(table)):
#         for p in permutations("xyzw"):
#             if [f(**dict(zip(p,r)))for r in table] == [0,0,0]:
#                 print(p)
# k = 0
# from itertools import *
# for x in product("ДЖОБС", repeat = 6):
#     s = "".join(x)
#     if s.count("Ж") <= 2 and s.count("Д") == 1 and s.count("О") == 1 and s.count("С") == 1:
#         k+=1
# print(k)
# k = 0
# for line in open("999"):
#     a = sorted(list(map(int, line.split())))
#     a1 = [i for i in a if a.count(i) == 1]
#     if len(a1) == 5:
#         if (2*(max(a) + min(a))) <= 3*(a[1] + a[2] + a[3]):
#             k += 1
# print(k)
#
# from math import *
# n = 26 + 26 + 10
# bit = ceil(log2(n))
# byteslovoidop = ceil(bit * 16 / 8) + 20
# for i in range(1,10000):
#     if i * byteslovoidop <= 10 * 1024:
#         print(i)


# a = (3*3125**9) + (2*625**7) + (3*125**6) - (2*25**5) - 2024
# d = []
# while a > 0:
#     d.append(a%25)
#     a = a//25
# print(d.count(0))

# from itertools import *
# def f(x,z,y,w):
#     return (w or y) and (x <= (not(z))) and (not(w))
# for x1,x2,x3,x4,x5 in product([0,1], repeat = 5):
#     table = [(x1,0,x2,0),(1,x3,x4,x5),(1,1,0,0)]
#     if len(table) == len(set(table)):
#         for p in permutations("xzyw"):
#             if [f(**dict(zip(p,r)))for r in table] == [1,1,1]:
#                 print(p)

# P = {2,4,6,8,10,12,14,16,18,20}
# Q = {5,10,15,20,25,30,35,40,45,50}
# A = []
#
# # На ДЕЛ
# def f(x):
#     return (x%33 != 0) <= (not(x%a != 0)) <= (not(x%242 != 0))
# for a in range(1,100):
#     k = 0
#     for x in range(1,1000000 + 1):
#         if f(x) == 1:
#             k += 1
#         else:
#             break
#     if k == 1000000:
#         print(a)

def f(x):
    return ((x & 112 != 0) or (x & 86 != 0)) <= ((x&65 == 0) <= (x&a)!=0)
for a in range(1,1000000):
    if all(f(x) == 1 for x in range(0, 10**6)):
        print(a)
