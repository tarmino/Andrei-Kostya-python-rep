"""
Шахматный ферзь ходит по диагонали, горизонтали или вертикали. 
Даны две различные клетки шахматной доски, 
определите, может ли ферзь попасть с первой клетки на вторую одним ходом.

Программа получает на вход четыре числа от 1 до 8 каждое, 
задающие номер столбца и номер строки сначала для первой клетки, 
потом для второй клетки. Программа должна вывести YES, 
если из первой клетки ходом короля можно попасть во вторую или NO в противном случае.
"""

c1=int(input())
r1=int(input())
c2=int(input())
r2=int(input())
if (c2==c1 or r2==r1) or (abs(c2 - c1) == abs(r2 - r1)):
	print('YES')
else:
	print('NO')

"""
Решение разработчиков

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')
"""