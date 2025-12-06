x = 5*216**1156 - 4*36**1147 + 6**1153 - 875
stri = []
kol5 = 0
kol0 = 0
while x > 0:
    stri += str(x%6)
    x = x//6
for i in stri:
    if i == "5":
        kol5 += 1
    elif i == "0":
        kol0 += 1
print(kol5 - kol0)
