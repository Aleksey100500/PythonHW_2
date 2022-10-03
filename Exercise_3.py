# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

number = int(input('Введите число: '))
nums = []
sum = 0
i = 0
print('Начало работы цикла.')
while i < number:
    formula = round(float((1 + 1 / (i+1)) ** (i+1)))
    nums.append(formula)
    sum += nums[i]
    i += 1
    print(nums)
print('Конец работы цикла.')
print(f'Сумма для n = {number}: {nums} -> {sum}')
