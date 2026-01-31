# def recursion(num):
#     return recursion (num * 2)

# school = [
#     [
#         ["a","b","c"], ["a","b","c"]
#     ],
#     [
#         ["a","b","c"], ["a","b","c"]
#     ]
# ]
# summ = 0
# def school_ref(school, summ = 0):
#     print(school)
#     if len(school) == 1:
#         return
#     for i in school:
#         return school_ref(i)
#
# school_ref(school)

a = [[1,2,3],
    [4,5],
     [6,7]]
# def rec(b):
#     # if type(b) == int:
#     #     return b + rec(b)
#     # return
#     if b == 1:
#         return 1
#     return b + rec(b - 1)
# g = rec(a)
# print(g)
# def rec(lst):
#     if not lst:
#         return 0
#     return lst[0] + rec(lst[1:])
# print(rec(a))

# def reverse_str(s):
#     result = ""
#     for char in s:
#         result += char + result
#     return result
# def reverse_rec(s):
#     if len(s) <= 2:
#         return s
#     return reverse_rec(s[::-1])
# print(reverse_rec('hello'))
import time
start1 = time.time()
def fact(s):
    result = 1
    for i in range(s):
        result *= i
    return result
print(fact(5))
print(time.time()-start1)
start2 = time.time()
def factorial_rec(n):
    if n == 1:
        return n
    return n * factorial_rec(n - 1)
print(factorial_rec(5))
print(time.time()-start2)