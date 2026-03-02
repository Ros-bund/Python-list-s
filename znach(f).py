# Считываем количество чисел (n)
kolichestvo = int(input())

# Создаем пустой список для хранения введенных чисел
chisla = []

# В цикле считываем сами числа и добавляем их в список
for i in range(kolichestvo):
    chislo = int(input())
    chisla.append(chislo)

# Выводим сначала все введенные числа
for chislo in chisla:
    print(chislo)

# Выводим пустую строку
print()

# Вычисляем и выводим значение функции для каждого числа
for chislo in chisla:
    znachenie = chislo**2 + 2*chislo + 1
    print(znachenie)