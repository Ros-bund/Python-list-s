# Считываем количество строк, которые введет пользователь
vsego_strok = int(input())

# Создаем список для хранения всех введенных предложений
spisok_fraz = []

# Заполняем наш список фразами
for i in range(vsego_strok):
    fraza = input()
    spisok_fraz.append(fraza)

# Считываем поисковый запрос (то, что мы ищем)
poiskoviy_zapros = input()

# Проходим по каждой сохраненной фразе
for fraza in spisok_fraz:
    # Приводим и фразу, и запрос к нижнему регистру для сравнения
    if poiskoviy_zapros.lower() in fraza.lower():
        # Если запрос нашелся внутри фразы, выводим оригинал
        print(fraza)