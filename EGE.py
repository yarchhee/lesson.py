from string import *
d = []
for x in printable[:21]:
    for y in printable[:21]:
        a = int(f'32{y}{x}a', 21) + int(f'16{y}18', 21)
        if a % 12 == 0 and int(y,21) % 2 != 0:
            print(a , x, y)




