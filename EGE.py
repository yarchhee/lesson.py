m = []
for x in range(1,7291):
    k = 0
    a = 27**298 + 27**269 - x
    while a > 0:
        if a%27 == 0:
            k+=1
        a//=27
    m.append(k)
print(max(m))



