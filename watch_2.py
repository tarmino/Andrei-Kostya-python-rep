"""
С начала суток часовая стрелка повернулась на угол в α градусов. 
Определите на какой угол повернулась минутная стрелка 
с начала последнего часа. 
Входные и выходные данные — действительные числа.
"""

a = float(input())
print((a/30 - int(a/30))*360)

"""
Решение разработчиков

alpha = float(input())
print(alpha % 30 * 12)
"""