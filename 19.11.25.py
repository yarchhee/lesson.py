# set = {
#     "key":"value",
#     "key1":[
#         1,2,3,4
#     ]
# } #словарь с элементом {ключ:значение} (dict)
# print(set["key"])
# print(set["key1"])
# print(set["key1"][2])

# my_dict = [
#     ("ключ1","значение1"),
#     ("ключ2","значение2"),
#     ("ключ3","значение3")
# ]
# print(my_dict, dict(my_dict))

# d = {} #dict
# d = {1,2} #set
# b = {str([1,2,3]):3, 3:5}
# print(b[str([1,2,3])])

# d = {"key1":"value1"}
# # print("key2" not in d ) # есть ли ключ  словаре d
# # b = [1,2,3]
# # b[0] = 100
# d["key1"] = 100
# d["key2"] = 1000
# del d["key1"]
# print(d)

# d = {"key1": "value1", "key2": "value2"}
# # for i in d:
# #     print(i, d[i], sep = ":")
# print(list(d.items())) #получает все элементы словаря как список кортежей
# for i,j in d.items():
#     print(i, j)
# print(list(d.values())) # возвращает список значений
# print(list(d.keys())) # возвращает список ключей

# print(d.get["key3", 10]) #get(key, value if not exist, el)
# print(d.pop("key2",10),d) #удаляет и возвращает значение

# print(d.popitem()) #удаляет и возвращает последний элемент

# d.update({"key3": "value3"}) #добавляет элемент
# print(d)

#d.clear()

# a = d.copy() #создает копию элемента в памяти
# a["key3"] = "value100"
# print(d, a)

# keys = ["key1", "key2", "key3", "key4"]
# new_dict = dict.fromkeys(keys, 10)
# print(new_dict)

#Задача 69
# a = {}
# a.update({"name":"alice"})
# print(a)

#Задание 71
# points = {"x":10}
# print(points.get("y", 10)

#Задание 75
# books = {"Романы":10, "детективы":5}
# books.update({"Фантастика":10})

# Задание 79
# marks = {"Информатика":5,
#          "Математика":5,
#          "Русский":3,
#          "История":4,
#          "Физика":4}
# ball = list(marks.values())
# sr = sum(ball)/len(ball)

#Задача 80
# a = input().split(" ")
# s = {}
# k = []
# for i in a:
#     key, value = i.split(":")
#     k.append((key, int(value)))
#     s[key] = int(value)
# print(s, "\n", dict(k))

#Задача 81
f = {}
students = ["Анна", 5, "Борис", 4, "Вера", 5]
for i in range(0,len(students),2):
    f[students[i]] = students[i+1]
print(f)