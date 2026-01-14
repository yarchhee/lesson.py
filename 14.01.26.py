# matrix = [[i*4 + j + 1 for j in range(4)]for i in range(4)]
# for row in matrix:
#     print(row)

# dicti = {i : i**3 for i in range(1, 11)}
# print(dicti)

# a = {i**2 for i in range(1, 21)}
# print(a)

# num = [2,4,6,8,10]
# res = []
# for i in num:
#     if i>7 and i%3 == 0:
#         res.append(True)
#     else:
#         res.append(False)
# print(any(res))

# password = "MyPass123"
# has_upper = [i.isupper() for i in password]
# has_lower = [i.islower() for i in password]
# has_digit = [i.isdigit() for i in password]
# alll = any([has_upper, has_lower, has_digit])
# print(alll)
#
# with open("901.txt") as f:
#     data = [list(map(int, i.split()))for i in f]
# def f1(line):
#     cnt_3 = [i for i in line if line.count(i) == 3]
#     cnt_1 = [i for i in line if line.count(i) == 1]
#     return len(cnt_3) == 6 and len(cnt_1) == 1
# def f2(line):
#     rep = [i for i in line if line.count(i) != 1]
#     norep = [i for i in line if line.count(i) == 1]
#     aver = sum(rep) / len(rep)
#     return aver < norep[0]
# for pos, val in list(enumerate(data, start = 1))[::-1]:
#     if f1(val) and f2(val):
#         print(pos)
#         break

# stroka = 0
# for line in open("911.txt"):
#     a = list(map(int, line.split()))
#     stroka += 1
#     a1 = [i for i in a if a.count(i) == 3]
#     a3 = [i for i in a if a.count(i) == 1]
#     sr = sum(a3) / len(a3)
#     if len(a1) == 3 and len(a3) == 3:
#         if sr < int(a1[-1]):
#             print(stroka)
# stroka = 0
# for line in open("913.txt"):
#     a = list(map(int, line.split()))
#     stroka += 1
#     a = sorted(a)
#     a1 = [i for i in a if a.count(i) == 1]
#     if len(a1) == 5:
#         if 2*(a[0] + a[4]) == 3 * (a[1] + a[2] + a[3]):
#             print(stroka)













