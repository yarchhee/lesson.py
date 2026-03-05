# На ДЕЛ
def f(x):
    return (x%33 != 0) <= (not(x%a != 0)) <= (not(x%242 != 0))
for a in range(1,100):
    k = 0
    for x in range(1,1000000 + 1):
        if f(x) == 1:
            k += 1
        else:
            break
    if k == 1000000:
        print(a)
def f(x):
    return ((x%2==0) <= (x%5!=0)) or (x+a>=70)
for a in range (1,100):
    if all(f(x)==1 for x in range (1,10**6)):
        print (a)
# Поразряд кон
def f(x):
    return ((x&84653 != 0) or (x&51763 != 0)) <= (x&a > 0)
for a in range(1,1000000):
    if all(f(x) == 1 for x in range(0, 10**7)):
        print(a)

# x и y
def f(x, y):
    return (3 * y + 2 * x < a) or (x > 8) or (y < 12)
for a in range(1,1000):
    if all(f(x,y) == 1 for x in range(1,1000) for y in range(1, 1000)):
        print(a)

# отрезки
def f(x):
    return (not(5 <= x <= 54) and (50 <= x <= 93)) <= (x > a)
for a in range(1,100):
    k = 0
    for x in range(1,1000):
        if f(x) == 0:
            k += 1
    if k == 20:
        print(a)