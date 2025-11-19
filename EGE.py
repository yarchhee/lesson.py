from math import *
alpha = 10 + 52 + 500
for len in range(1,100000):
    bit = ceil(log2(alpha))
    byte_1_nomer = ceil(bit * len /8)
    if 45877 * byte_1_nomer > 49 * 1024 * 1024:
        print(len)
        break
