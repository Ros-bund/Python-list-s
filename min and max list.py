# 1. Считываем строку и превращаем её в список целых чисел
vhodnie_dannye = input().split()
chisla = [int(s) for s in vhodnie_dannye]

# 2. Находим индекс минимального и максимального элементов
# Метод index() возвращает позицию первого встретившегося элемента
indeks_minimuma = chisla.index(min(chisla))
indeks_maximuma = chisla.index(max(chisla))

# 3. Меняем элементы местами с помощью "кортежной распаковки"
# Это самый элегантный способ в Python поменять значения без временной переменной
chisla[indeks_minimuma], chisla[indeks_maximuma] = chisla[indeks_maximuma], chisla[indeks_minimuma]

# 4. Выводим список, превратив числа обратно в строки через пробел
print(*chisla)