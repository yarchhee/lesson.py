# def find(st:str, substring:str):
#     for i in range(len(str)):
#         flag = True
#         for j in range(len(substring)):
#             if substring[j] != st[i+j]:
#                 flag = False
#                 break
#         if flag:
#             return i
#     return -1
import string

# def reverse(lst):
#     a = []
#     for i in lst:
#         a.append(lst[len(lst)-1])
#         lst.remove(lst[-1])
#     return a
# print(reverse([1,2,3,4,5]))

# def reverse(a):
#     b = []
#     for i in range(len(a)-1,-1,-1):
#         b.append(a[i])
#     return b
# a = list(map(int, input().split()))
# print(reverse(a))


# def index(lst, el):
#     for i in range(len(lst)):
#         if lst[i] == el:
#             return i
#     return "Элемент не найден"
# print(index())

# def count(b):
#     a = {}
#     for i in b:
#         i.lower()
#         a[i] = b.count(i)
#     return a
# b = list(map(str, input().split()))
# print(count(b))

# def func(string):
#     string = string.lower()
#     lst_string = string.split()
#     set_lst_string = set(lst_string)
#     s = {}
#     for item in set_lst_string:
#         s[item] = lst_string.count(item)
#     return s
# func(input())

# d - десятичная
# print(f'{27:d}') # десятичная СС int
# # b - двоичная bin
# print(f'{27:b}')
# # о - восьмеричная oct
# print(f'{27:o}')
# # x - шестнадцатиричная hex
# print(f'{27:x}')
#
# a = 1.28342732
# print(f'{a:2f}')

from string import *
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)
# print(string.whitespace)




