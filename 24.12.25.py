# st1 = input()
# st2 = input()
# st1_1 = st1.split(" ")
# if len(st2) == len(st1_1[0]):
#     list(st2)
#     list(st1_1[0])
#     if st2 == st1_1[0]:
#         print("True")
# else:
#     print("False")

# st = input()
# substring = input()
# k = 0
# st = st.split(" ")
# for i in st:
#     if i == substring:
#         k+=1
# print(k)

def replace(st, old, new):
    string = "" #итоговая строка
    if old not in st: #Подсроки есть в строке?
        return False
    i = 0 #индекс элемента текущего
    while i < len(st): #пока индекс меньше текущей длинны
        flag = False #Найдены ли совпадения?
        for j in range(len(old)):
            if st[i + j] != old[j]:# ищем посимвольно из исходной и строки
                flag = True #совпадений не найдено
                break
        if not flag:#если найдено совпадение
            string += new#добавляем в строку новую подстроку
            i += len(old) #прибавляем на длинну старой строки
        else:#если совпадений не найдено
            string += st[i] #добавляем в текущую строку символ
            i += 1#перешагиваем на следующий символ
    return string




