# Дано натуральное число N. Найдите значение выражения:N + NN + NNN
# N может быть любой длины.
number = input('Введите число: ')
result = int(number)+int(number+number)+int(number+number+number)
print(result)