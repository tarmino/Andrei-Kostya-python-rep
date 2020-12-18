"""
Дано два числа a и b. Выведите гипотенузу треугольника с заданными катетами.
"""

import math
a = int(input())
b = int(input())
print(math.sqrt(a**2 + b**2))

"""
Решение разработчиков

import math

a = int(input())
b = int(input())
c = math.sqrt(b*b + a*a)
print(c)
"""