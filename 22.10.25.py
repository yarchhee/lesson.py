# a=[[1,2,3],[4,5,6]]
# print(a[0])
# print(a[1])
# print("-"*10)
# for index in range(0,len(a)):
#     print(a[index][1])
#range - генерирует список элементов в промежутке от и до
#len - длина объекта
# a=[[1,2,3],[4,5,6]]
# b=[[0,0],[0,0]]
# for i in range(len(a)):
#     for j in range(len(a[0])):
#         b[j][i]=a[i][j]
# for i in b:
#     print(i)

b="1234567890"
counter=0
while True:
    a=input("Введите пароль: ")
    if counter ==2:
        print("Try next time")
        break
    counter+=1
    if len(a)<8:
        print("Пароль короткий")
    else:
        k=False #есть ли в пароле число?
        for i in b:
            if i in a:
                k=True
                break
        if k:
            print("Пароль верный")
        else:
            print("Пароль неверный")


a=[[[1,2],[3,4]],[[5,6],[7,8]]]
b=[[0,0],[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(a[i])):
        for z in range(len(a[i][j])):
            print(a[i][j][z])


