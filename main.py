from math import *

def degree_1(n):
    return ceil(log2(n))


def degree_2(n):
    x = 1
    while (x <= n):
        x <<= 1
    return int(log2(x))