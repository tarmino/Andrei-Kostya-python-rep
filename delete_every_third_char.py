"""
Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.
"""

S = input()
for i in range(len(S)):
	if i%3 != 0:
		print(S[i], end='')

"""
Решение разработчиков

s = input()
t = ''
for i in range(len(s)):
    if i % 3 != 0:
        t = t + s[i]
print(t)
"""