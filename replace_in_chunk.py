"""
Дана строка. 
Замените в этой строке все появления буквы h на букву H, 
кроме первого и последнего вхождения.
"""

S = input()
d = S[S.find('h')+1:S.rfind('h')]
print(S[:S.find('h')+1] + d.replace('h','H') + S[S.rfind('h'):])

"""
Решение разработчиков

s = input()
a = s[:s.find('h') + 1] 
b = s[s.find('h') + 1:s.rfind('h')]
c = s[s.rfind('h'):]
s = a + b.replace('h', 'H') + c
print(s)
"""