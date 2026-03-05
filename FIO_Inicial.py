# Считываем строку (например: "Иванов Иван Иванович")
polnoe_fio = input()

# Разбиваем строку на список слов: ['Иванов', 'Иван', 'Иванович']
spisok_slov = polnoe_fio.split()

# Достаем первую букву каждого слова и добавляем точку
inicial_familii = spisok_slov[0][0] + "."
inicial_imeni = spisok_slov[1][0] + "."
inicial_otchestva = spisok_slov[2][0] + "."

# Выводим всё в одну строку без пробелов (или с ними, смотря какой тест)
# Чаще всего в таких задачах требуют формат И.И.И.
print(inicial_familii + inicial_imeni + inicial_otchestva)