# def analyze_text(text):
#     letters = len(text)
#     words = text.count(" ")
#     sentences = text.count(".") + text.count("!") + text.count("?")
#     return letters, words + 1 , sentences
# print(analyze_text(input()))

# def calculate_area(shape = "rectangle", length = 0, width = 0, radius = 0):
#     area = 0
#     if shape == "rectangle":
#         area = length * width
#     elif shape == "circle":
#         area = 3.14 * radius**2
#     return area
# print(calculate_area(input()))

# def format_name(first, last, middle = "", title = ""):
#     name = ""
#     if title != "":
#         name = title +' '+ first+' ' + last+ ' ' + middle
#     else:
#         name =  first+' ' + last+ ' ' + middle
#     return name
# print(format_name(input(), input(), input(), input()))

# def f(*args):
#     return list(set(args))
# print(f(input()))

# from random import randint
# def sosiski(first, last):
#     pervoe = []
#     maxi = 0
#     for i in range(50):
#         pervoe.append(randint(first, last))
#     for i in pervoe:
#         if pervoe.count(i) >= maxi:
#             maxi = i
#     return(pervoe,maxi,i)
# print(sosiski(input(),input()))










