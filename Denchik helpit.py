a1 = [1,2,3]
a2 = [10,20,30]

def yarik(a,b):
    return a*b

result = list(map(yarik, a1, a2))
print(result)