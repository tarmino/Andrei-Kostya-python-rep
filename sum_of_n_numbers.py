"""
Дано несколько чисел. Вычислите их сумму. 
Сначала вводите количество чисел N, 
затем вводится ровно N целых чисел. 

Какое наименьшее число переменных нужно для решения этой задачи?
"""

N = int(input())
sum = 0
for i in range(N):
	number = int(input())
	sum = sum + number
print(sum)


"""
Решение разработчиков

n = int(input())
sum = 0
for i in range(n):
    sum += int(input())
print(sum)
"""