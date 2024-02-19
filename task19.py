# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

from random import randint

list = []

size = int(input("Write number: "))

for i in range(size):
    list.append(randint(0, 10))
print(*list)

step = int(input('Write step: '))%len(list)
list = list[-step::]+list[:-step]
print(*list)