a = open("9.txt")
total = 0
for string in a:
    d = string.split()
    d = list(map(int, d))
    print(d)
    for i in d:
        if d.count(i) == 3 and i%2 != 0:
            total += 1





