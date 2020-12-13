"""
Шахматный конь ходит буквой “Г” — на две клетки по вертикали в любом направлении 
и на одну клетку по горизонтали, или наоборот. 
Даны две различные клетки шахматной доски, 
определите, может ли конь попасть с первой клетки на вторую одним ходом.

Программа получает на вход четыре числа от 1 до 8 каждое, 
задающие номер столбца и номер строки сначала для первой клетки, 
потом для второй клетки. Программа должна вывести YES, 
если из первой клетки ходом короля можно попасть во вторую или NO в противном случае.
"""

c1=int(input())
r1=int(input())
c2=int(input())
r2=int(input())
if abs(c2-c1) == 2 and abs(r2-r1) == 1 or abs(r2-r1) == 2 and abs(c2-c1) == 1:
	print('YES')
else:
	print('NO')

"""
Решение разработчиков

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
dx = abs(x1 - x2)
dy = abs(y1 - y2)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('YES')
else:
    print('NO')
"""