"""
Дано 10 целых чисел. 
Вычислите их сумму. 
Напишите программу, использующую наименьшее число переменных.
"""

s = 0
for i in range(10):
	a = int(input())
	s = s + a
print(s)

"""
Решение разработчиков

sum = 0
for i in range(10):
    number = int(input())
    sum += number
print(sum)
"""