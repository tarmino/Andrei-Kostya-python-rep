"""
По данному натуральному n вычислите сумму 13+23+33+...+n3.
"""

n = int(input())
s = 0
for i in range(n+1):
	s = s + i**3
print(s)

"""
Решение разработчиков

n = int(input())

sum = 0
for i in range(1, n + 1):
    sum += i ** 3

print(sum)
"""