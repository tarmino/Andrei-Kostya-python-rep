"""
Дана строка, в которой буква h встречается как минимум два раза. 
Разверните последовательность символов, 
заключенную между первым и последним появлением буквы h, в противоположном порядке.
"""

S = input()
print(S[:S.find('h')+1] + S[S.rfind('h')-1:S.find('h'):-1] + S[S.rfind('h'):])


"""
Решение разработчиков

s = input()
a = s[:s.find('h')] 
b = s[s.find('h'):s.rfind('h') + 1]
c = s[s.rfind('h') + 1:]
s = a + b[::-1] + c
print(s)
"""