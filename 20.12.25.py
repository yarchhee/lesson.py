# numbers = list(map(int, input().split()))
# print(numbers[::2])
# print(numbers.index(min(numbers)))
# numbers.remove(max(numbers))
# print(sorted(numbers, reverse=True))

# list_1 = [1, 2, 3, 4, 2, 3, 4, 6, 8]
# list_2 = list(map(int, input().split()))
# print(tuple(set(list_1).intersection(list_2)))

#ASCI - таблица
# print(ord("Y"))
# print(chr(72))

a = input()
b = ""
for i in a:
    if 65 <= ord(i) <= 90:
        b+=chr(ord(i) + 32)
    else:
        b+=i
print(b)








