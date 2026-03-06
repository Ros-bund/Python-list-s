# Считываем строку с числами (например: "3 7 2")
vvedennaya_stroka = input()

# Разбиваем строку на отдельные элементы (пока это строки текста)
spisok_teksta = vvedennaya_stroka.split()

# Проходим по каждому элементу в списке
for element in spisok_teksta:
    # Превращаем текст в целое число
    chislo = int(element)
    
    # Печатаем символ '#' столько раз, каков размер числа
    # В Python можно просто умножить строку на число!
    print('+' * chislo)