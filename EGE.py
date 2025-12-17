a = 9**12 + 3**8 - 3
b = []
while a>0:
    b.append(a%3)
    a = a//3
print(b.count(2))







