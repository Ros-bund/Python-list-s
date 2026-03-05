# Считываем входную строку текста
vvedennaya_stroka = input()

# Разбиваем строку на список слов по пробелам
spisok_slov = vvedennaya_stroka.split()

# Проходим циклом по списку и выводим каждое слово отдельно
for slovo in spisok_slov:
    print(slovo)