import math
import random

v = 100
print(v)


def square(num):
    sq = num * num
    return sq
    pass


def generator():
    num1 = random.randrange(100)
    return num1
    pass


print(square(4))
print(generator())
