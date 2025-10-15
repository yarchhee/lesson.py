#пока условие
#бесконечный цикл если True
# while True: #while условие, например: (a>10)
#     print("Hello")

#for переменная in итерируемый обьект
#list
#1:1
#3:3
#2:2
#string
# a="wdda"
#print(a[0])
#в переменную i записываются элементы
# посимвольно
#для каждой итерации цикла
# for i in "wdda":
#     print(i)

#range (начало, конец, шаг)
#генерирует список (генеатор) чисел от
#начало до конец - 1
# print(list(range(0,10)))
# print(list(range(10,0,-1)))
# for i in range(10):
#     print(i)

#break - останавливает выполнение
#continue - останавливает итерацию
# counter = 0
# counter_false = 0
# while True:
#     counter += 1
#     if counter % 3 != 0:
#         counter_false += 1
#         continue
#     print("наше значение:", counter)
#     if counter >= 100:
#         break
# print("это количество некратных", counter_false)

# a = [[1,2,3,4], [1,2,3,4], [1,2,3,4]]
# # print(a[0][0])
# for i in a:
#     print(i[0],i[0])
#
# a = [[1,2,3,4], [1,2,3,4], [1,2,3,4]]
# for i in a:
#     for j in i:
#         print(j)

a = [[1,2,3,4], [1,2,3,4], [1,2,3,4]]
i = 0
j = 0
#len() - возвращает длину обьекта
# print(len(a))
# print(len(a[0]))
# print(a[len(a)-1])
# while i < len(a):
#     while j < len(a[0]):
#         print(a[i][j])
#         j += 1
#     i+=1
#
# a = [1,2,3]
#отрицательный индекс получает
# элемент с обратной стороны
# print(a[-2])

# for i in range(0,11):
#     print(i)
#
# n=int(input())
# for i in range(0,n):
#     print(i^2)


for i in range(1,20):
    if i%3 == 0 :
        continue
    print(i)
print("gotovo")