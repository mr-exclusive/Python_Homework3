# 6. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на |K| элементов вправо, если K – положительное и влево, если отрицательное.

list_orig = [5, 3, 7, 4, 6]
k = int(input('Enter a number, how far to move array elements: '))
k = k % len(list_orig)
list_result = [0] * len(list_orig)

for i in range(len(list_orig)):
    if i < k:
        list_result[i] = list_orig[len(list_orig) - k + i]
    else:
        list_result[i] = list_orig[i - k]

print(list_result)
