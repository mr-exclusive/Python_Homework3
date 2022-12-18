# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Enter a number: '))

list_right = []
n0 = 0
n1 = 1

for i in range(n + 1):
    list_right.append(n0)
    x = n0 + n1
    n0 = n1
    n1 = x

list_left = []
for i in range(len(list_right) - 1, 0, -1):
    list_left.append(list_right[i] * (-1) ** (i + 1))

print(list_left + list_right)
