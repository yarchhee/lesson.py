from math import *
for l in range(1,1000):
    kod = 10+52+500
    bit = ceil(log2(kod))
    byte = ceil(l*bit/8)
    if 45877*byte > 49*1024*1024:
        print(l)
        break
