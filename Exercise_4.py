# * 4. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15
num = int(input('Number of elements: '))
numbers = []
i = 0
while i <= num * 2:
    formula = -num + i
    numbers.append(formula)
    i += 1
print(numbers)

posone = int(input('Position one: '))
postwo = int(input('Positione two: '))
mult = numbers[posone - 1] * numbers[postwo - 1]
print(f'Product of numbers: {mult}')