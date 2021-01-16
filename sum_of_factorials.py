"""
По данному натуральном n вычислите сумму 1!+2!+3!+...+n!. 
В решении этой задачи можно использовать только один цикл. 

Пользоваться математической библиотекой math в этой задаче запрещено.
"""

n = int(input())
f = 1
s = 0
for i in range(1, n + 1):
	f = f * i
	s = s + f
print(s)

"""
Решение разработчиков

n = int(input())
partial_factorial = 1
partial_sum = 0
for i in range(1, n + 1):
    partial_factorial *= i
    partial_sum += partial_factorial
print(partial_sum)
"""