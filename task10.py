# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

import random

number = int(input("Enter number: "))
num = random.randint(0,1)
print(num, end=' ')
count = 0

for i in range(number-1):
    num = random.randint(0,1)
    print(num, end=' ')
    if num == 0:
        max = num
        count+=1

print(f'\n {count}')