"""
Даны три целых числа. Определите, сколько среди них совпадающих. 

Программа должна вывести одно из чисел: 
3 (если все совпадают), 
2 (если два совпадает) или 
0 (если все числа различны).
"""

a = int(input())
b = int(input())
c = int(input())
s = 0
if a == b or b == c or c == a:
	s = 2
if a == b and b == c:
	s = s + 1
print(s)

"""
Решение разработчиков

a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)
"""