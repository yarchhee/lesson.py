#Задача 29
from random import randint
l = []
for i in range(20):
    l.append(randint(0,10))
print(set(l))
# # s = l[0]
# # l[0] = l[-1]
# # l[-1] = s
# l[0],l[-1] = l[-1],l[0]
# print(l)

#Задача 25
# nums = [1,2,3,4,5,6]
# sr = int(sum(nums)/len(nums))
# for i in nums:
#     if i == sr:
#         print(i)
#         nums.remove(i)
# print(nums)

#Задача 23
# a = [1,2,21,2,4,3,1,5,96,4,3,4]
# k = []
# for i in range(1,len(a)-1):
#     if a[i] > a[i+1] and a[i] > a[i-1]:
#         k = [a[i],i]
#         break
# print(k[0], k[1], a.index(k[0]))

#Задача 21
a = input().split()
h = []
for i in a:
    if i not in h and a.count(i) < 2:
        h.append(i)
print(h)

#Задача 31
a = [2,4,2,9,8,3,4,2,1,9,3,2,8,5,9]
maxim = 0
cash = []
for i in range(len(a)):
    seen = []
    for j in range(i, len(a)):
        if a[j] in seen:
            break
        seen.append(a[j])
    if len(seen) > maxim:
        maxim = len(seen)
        cash = seen
print(maxim, sum(cash),cash)

