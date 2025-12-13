# with open("task_6.txt") as f:
#     cur_len = 1
#     a = f.read()
#     for i in range(1,len(a)-1):
#         if (a[i].isdigit() and a[i-1].isdigit()) or \
#             (a[i].isalpha() and a[i-1].isdigit()) :
#             cur_len += 1
#         else:
#             max_len = max(max_len,cur_len)
# print(max_len)

# with open("1700.txt") as f:
#     data = list(map(int, f))
#     min_el = min(data)
#     answer = []
#     for i in range(len(data) - 1):
#         z = data[i]
#         y = data[i+1]
#         if z % 16 == min_el or y % 16 == min_el:
#             answer.append(z+y)
#     print(len(answer), max(answer))

# with open("1710.txt") as f:
#     data = list(map(int, f))
#     max_el = max(data)
#     k = 0
#     answer = []
#     for i in range(len(data)):
#         z = data[i]
#         y = data[i+1]
#         if z+y == max_el:
#             answer.append(z**2 + y**2)
#     print(len(answer), max(answer))

# with open("1710.txt") as f:
#     data = list(map(int, f))
#     max_el = max(data)
#     answer = []
#     for i in range(len(data)-1):
#         z = data[i]
#         y = data[i+1]
#         if z + y == max_el:
#             answer.append(z**2 + y**2)
#     print(len(answer),max(answer))

def f(x,l):
    return (10<= i <=99) ^ (10<=l<=99)
with open("1716.txt") as f:
    data = list(map(int, f))
    min_el = 9999999
    for i in data:
        if 10<=i<=99:
            if min_el>i:
                min_el = i
    answer = []
    for i in range(len(data)- 1):
        z = data[i]
        y = data[i+1]
        if f(z,y) and ((z+y)% min_el) == 0:
            answer.append(z+y)
    print(len(answer), max(answer))



