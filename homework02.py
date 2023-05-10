import random
numbers = [random.randint(1, 9) for _ in range(15)]
print("Исходный массив: ", numbers)
number = input("Введите трёхзначное натуральное число: ")
numbers_array = "".join(str(x) for x in numbers)
if number in numbers_array:
    print("Последовательность существует.")
else:
    print("Последовательность не существует.")