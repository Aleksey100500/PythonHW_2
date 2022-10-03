# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

number = float(input('Введите число: '))
sum = 0
newNumber = number * 100
while newNumber > 0:
    ost = int(newNumber % 10)
    sum += ost
    newNumber = newNumber // 10
print(sum)