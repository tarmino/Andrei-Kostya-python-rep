"""
Для настольной игры используются карточки с номерами от 1 до N. 
Одна карточка потерялась. Найдите ее, зная номера оставшихся карточек.
Дано число N, 
далее N − 1 номер оставшихся карточек (различные числа от 1 до N). 
Программа должна вывести номер потерянной карточки.

Для самых умных: массивами и аналогичными структурами данных пользоваться нельзя.
"""

N = int(input())
sum_total = 0
sum_present = 0
for i in range(1, N + 1):
	sum_total = sum_total + i
for j in range(1, N):
	card = int(input())
	sum_present = sum_present + card
lost = sum_total - sum_present
print(lost)
	 
"""
Решение разработчиков

n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i
# можно доказать формулу:
# sum == n * (n + 1) // 2
# но мы посчитаем это значение циклом
for i in range(n - 1):
    sum -= int(input())
print(sum)
"""