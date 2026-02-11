# задание 1
print("╔══════════════════════════════════════════════════════════╗")
print("║                     ФИНАНСОВЫЙ ОТЧЕТ                     ║")
print("╠══════════════════════════════════════════════════════════╣")
for line in open("transact"):
    a = list(map(str, line.replace("\n", "").split(', ')))
    print(f"║ {a[0]} │        {a[1]}        │            {a[2]} ║")
print("╠══════════════════════════════════════════════════════════╣")
print("║                              ИТОГО:           28480.32 ₽ ║")
print("╚══════════════════════════════════════════════════════════╝")



# Задание 2
# s200 = []
# s401 = []
# s403 = []
# s404 = []
# s500 = []
# for line in open("acces"):
#     a = str(line)
#     if "200" in a:
#         s200.append(a)
#     elif "401" in a:
#         s401.append(a)
#     elif "403" in a:
#         s403.append(a)
#     elif "404" in a:
#         s404.append(a)
#     elif "500" in a:
#         s500.append(a)
# print(s200)

# задание 3
# counter = 0
# spisok = []
# for a in open("triples"):
#     spisok.append(int(a))
# for i in range(len(spisok) - 2):
#     a = spisok[i]
#     b = spisok[i + 1]
#     c = spisok[i + 2]
#     maxim = max(a, b, c)
#     minim = min(a, b, c)
#     usl1 = (a%5 == minim) or (b%5 == minim) or (c%5 == minim)
#     if usl1 == True:
#         counter += 1
# print(f"количество троек: {counter}")

# # задание 6
# def log_action(func):
#     def wrapper(*args, **kwargs):
#         print(f"Выполняется {func.__name__} ...")
#         result = func(*args, **kwargs)
#         print(f'{func.__name__} завершена')
#         return f'Результат: {result}'
#     return wrapper
#
# @log_action
# def read_sales(filename):
#     spisok = []
#     for line in open(filename):
#         a = tuple(line.split())
#         spisok.append(a)
#     return spisok
# print(read_sales("transact"))
#
# @log_action
# def get_total_by_category(category):
#     sumer = 0
#     for line in open("transact"):
#         a = list(map(str, line.replace("\n", "").split(', ')))
#         if a[1] == category:
#             sumer += float(a[2])
#     return sumer
# print(get_total_by_category("Аренда"))
#
# @log_action
# def get_average_by_sale():
#     k = 0
#     sumi = 0
#     for line in open("transact"):
#         k+=1
#         a = list(map(str, line.replace("\n", "").split(', ')))
#         suma = float(a[2])
#         sumi += suma
#     return sumi / k
# print(get_average_by_sale())

