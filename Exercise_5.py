# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

num = int(input('Введите число: '))
numbers = []
for i in range(0, num):
    numbers.append(i)
print(numbers)
newNumbers = []
while num > 0:
    num -= 1
    newNumbers.append(numbers[num])
print(newNumbers)
# Пока больше ничего не придумал(