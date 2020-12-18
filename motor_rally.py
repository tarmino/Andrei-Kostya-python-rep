"""
За день машина проезжает n километров. 
Сколько дней нужно, чтобы проехать маршрут длиной m километров? 

Программа получает на вход числа n и m.
"""

import math
n = int(input())
m = int(input())
print(math.ceil(m/n))

"""
Решение разработчиков

from math import ceil

n = int(input())
m = int(input())
print(ceil(m / n))
"""