# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

from random import randint

list = []

size = int(input('Write number: '))
count = 0

for i in range(size):
    list.append(randint(0, 9))
print(list)

for i in range(len(list) - 1):
    if list[i] > list[i+1]:
        count+=1
print(count)
    