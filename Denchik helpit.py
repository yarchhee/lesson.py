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
ns=1000
st=10/100
t=3
counter=0
while counter<t:
    ns = (ns*st)+ns
    print(round(ns,3))
    counter+=1