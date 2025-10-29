# a1 = [1,2,3]
# a2 = [10,20,30]
#
# def yarik(a,b):
#     return a*b
#
# result = list(map(yarik, a1, a2))
# print(result)
# 5.
# for i in range(1,5):
#    for j in range((4-i),-1,-1):
#        print("*"*i+" "*j)
#        break

#
#

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i<5:
#         print(i)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for i in a:
    for j in b:
        if i==j:
            print(i, end=",")


