a = input()
b = set()
d = {}
for i in a:
    b.add(i)
for j in b:
    d.update({j:a.count(j)})
print(d)


