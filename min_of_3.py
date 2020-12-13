"""
Даны три целых числа. Выведите значение наименьшего из них.
"""

a = int(input())
b = int(input())
c = int(input())
if a < b:
	if a < c:
		print(a)
	else:
		print(c)
else:
	if b < c:
		print(b)
	else:
		print(c)

"""
Решение разработчиков

a = int(input())
b = int(input())
c = int(input())
if b >= a <= c:
    print(a)
elif a >= b <= c:
    print(b)
else:
    print(c)
"""