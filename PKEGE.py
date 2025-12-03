from math import *
alphabet = 26 + 26 + 10
bit = ceil(log2(alphabet))
byteslovo = ceil(bit * 16 / 8)
for i in range(1,100000):
    if (byteslovo + 20) * i <= 10 * 1024:
        print(i)