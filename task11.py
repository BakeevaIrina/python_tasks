# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 

number = int(input('Enter number: '))

fib1 = 0
fib2 = 1
n = 2

while number > fib2:
    t = fib1
    fib1 = fib2
    fib2 = t + fib2
    print(fib2, end=' ')
    n += 1
print(f'The number {number} on the count is {n} ')