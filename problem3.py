# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
#
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

arr = [1.1, 1.2, 3.1, 5, 10.01]
fractions = []

for i in arr:
    fractional_part = round(i % 1, 5)
    if fractional_part != 0:
        fractions.append(fractional_part)

print(fractions)
print(f'The difference between min and max fractional portions is {max(fractions) - min(fractions)}.')
