# открытие файла маршрут/режим открытия/кодировка при чтении/записи
# file = open("test.txt", "r", encoding="utf-8")
# print(file.read()) # cчитывает все строки текстового файла
# print(file.readline()) # считывает одну строку из файла
# print(file.readlines()) #  считывает файл как список строк

# r - чтение
# w - запись
# a - добавить в конец файла
# x - открывает файл для записи только если он не существует

# rb, wb, ab, xb - бинарные действия

# r+/x+ - открывает файл для чтения и записи(файл должен существовать)
# w+/a+ - открывает файл для записи если файла нет он его создаст

# print(file.read()) # курсор в начале первой строки
# print(file.read()) # курсор в начале второй строки
# print(file.read()) # курсор в начале третьей строки
# print(file.read()) # курсор в начале четвертой строки

# print(file.read(10))
# print(file.tell()) # позиция указателя (число)

# file.seek(0)
# print(file.read(10))

# file.close() # закрытие файлов

# контекстный менеджер
# with open("test.txt", "r", encoding="utf-8") as file:
#     # file_item = file.readline()
#     # while file_item:
#     #     print(len(file_item)-1)
#     #     file_item = file.readline()
#     for file_item in file.readlines():
#         print(len(file_item)-1)

# with open("test.txt", "w", encoding="utf-8") as file:
#     file.write("hello")
# with open("test.txt", "a", encoding="utf-8") as file:
#     file.write("\nhello")
# with open("test.txt", "x", encoding="utf-8") as file:
#     file.write("\nhello")

# s = ["hello\n","world"]
# with open("test.txt", "r+", encoding="utf-8") as file:
#     file.writelines(s)

#задача 1
# s = ["wer","sd","sdf"]
# with open ("test.txt", "w+", encoding="utf-8") as file:
#     file.writelines(s)
# with open ("test.txt", "r", encoding="utf-8") as file:
#     print(file.read())



