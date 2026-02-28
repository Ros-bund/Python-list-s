n = int(input())
numbers = []

# Считываем n чисел и добавляем их в список
for _ in range(n):
    numbers.append(int(input()))

# Выводим сначала все отрицательные числа
for num in numbers:
    if num < 0:
        print(num)

# Затем выводим все нули
for num in numbers:
    if num == 0:
        print(num)

# В конце выводим все положительные числа
for num in numbers:
    if num > 0:
        print(num)