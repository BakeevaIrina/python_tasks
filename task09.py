# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N 
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# Input: 5
# Output: 120 

number = int(input('Enter digit: '))
i = 1
multi = 1
while i<=number:
    multi = multi * i
    i += 1
print(f'!{number} = {multi}')