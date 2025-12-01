# #Задача 85
# a = input().split()
# b = input().split()
# A = {}
# B = {}
# Aa = set(a)
# Bb = set(b)
# for i in Aa:
#     A.update({i: a.count(i)})
# for i in Bb:
#     B.update({i: b.count(i)})
# d = {}
# for key, values in A.items():
#     if key not in B:
#         B[key] = values
#     else:
#         B[key] += values
# print(B)

#Задача 86
# a = input().split()
# b = {}
# A = set(a)
# d = sorted(list(A))
# g = {}
# for i in d:
#     b.update({i: a.count(i)})
#     if b[i] > 1:
#         g.update({i: b[i]})
# print(g)

#Задача 88
# students = [
#     {'name': 'Alice', 'group': 'A', 'score': 85},
#     {'name': 'Bob', 'group': 'B', 'score': 92},
#     {'name': 'Charlie', 'group': 'A', 'score': 78},
#     {'name': 'David', 'group': 'C', 'score': 88},
#     {'name': 'Eve', 'group': 'B', 'score': 95}
# ]
# s = {}
# for student in students:
#     if student['group'] in s:
#         s[student['group']].append(student['name'])
#     else:
#         s[student['group']] = [student['name']]
# print(s)

#Задача 87
# a = input().replace(' ','')
# A = {}
#
# for i in a:
#     A[i] = a.count(i)
# s = [
#     ["",0],
#     ["",0],
#     ["",0]
# ]
# for i in A:
#     for j in range(len(s)):
#         if s[j][1] < A[i]:
#             s[j][0] = i
#             s[j][1] = A[i]
#             break
# print(A)
# print(s)










