# a="hello"
# print(ord(a[0]),chr(104))

# a="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
# for i in a:
#     print(ord(i),i)
# print("q"<"w")
#
# a="10"
# print(int(str(a),16))
#
# print("\n\t")
# print('\'')
# print("\U0001F600")
# g=r"https://dnevnik.edumil.ru/component/dnevnik/?controller=dnevnik&task=dnevnik"
# print(g)
#
# name="Миша"
# #s[n:m:k]
# #n - начало среза
# #m - конец среза
# #k - шаг среза
# print(name[0:4:2])
# #Мш
# print(name[-1])
# print(name[::-1])

string="hello world"

print(string.find("w"))# поиск первого схождения подстроки
print(string.index("d"))# возвращает индекс подстроки если такого символа нет ошибка
print(string.rfind("w"))# поиск схождения с последнего символа
print(string.split(" "))# делит строку по разделителю " "
print(string.count(" ")) #считает количество подстрок
print(string.lower()) #делает текст в нижнем регистре
print(string.upper()) # поднимает текст с колен (верхний регистр)
print(string.isdigit()) # все символы строки это числа?
string=("hello")
print(string.isalpha())#True если нет пробелов и цифр в строке
print(string.isalnum())#2 верхних метода в один
string="***hello world***"
print(string.strip("*"))#удаляет выбранный символ в начале и конце строки
#replace(символ, на что меняем, сколько раз)
print(string.replace("*", "#",2))
l=["h","e","l","l"]
print("".join(l))#соединяет элементы с разделителями


#1
h=input()
print(h[-4:])
#2
b=input()
print(b[0::2])