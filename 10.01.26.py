# b = []
# for i in range(5):
#     b.append(i)
# print(b)


# [выражение for элемент in последовательность if условие]
# b = [i for i in range(5)]
# print(b)

# x = [i for i in range(5) if i %2 == 0]
# print(x)

# nums = [1, -1, -2, -3, -4, 3]
# a = [x**2 for x in nums if x > 0]
# print(a)

# b = []
# for i in range(10):
#     for j in range(10):
#         b.append(i*j)

# matrix = [[row * col for col in range(1,4)] for row in range(1,4)]
# flatten_matrix = [item for row in matrix for item in row]
# print(matrix)
# print(flatten_matrix)

# dict_test = {i : i**2 for i in range(1,6)}
# print(dict_test)

# set_test = [i for i in range(10)]
# print(set_test)

# tuple_test = tuple(x for x in range(10))
# print(tuple_test)

# pairs = {(x,y) for x in range(1,4) for y in range(1,4)}
# print(pairs)

# a = [i**2 for i in range(1,16)]

# x = ['python', 'java', 'c++', 'javascript', 'go']
# a = [b.upper() for b in x]
# print(a)

# a = [0, 15, 20, 25, 30, -5, -10]
# x = [f*9/5+32 for f in a if f>0]

# a = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
# x = [z for x in a for z in x if z%2 == 0]
# print(x)

# a = ["apple", "banana", "cherry", 'date', 'elderberry']
# z = {x : len(x) for x in a if len(x)>5  }

# names = ["Привет мир!", 'Программирование', 'Списочные включения']
# a = {i : [len(j) for j in i.split(' ')] for i in names}

# a = {i : [j for j in range(1, i + 1) if i % j == 0] for i in range(1, 6)}
# print(a)
