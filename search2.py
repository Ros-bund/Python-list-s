# 1. Считываем количество исходных строк
nomer_strok = int(input())
vse_frazi = []

for i in range(nomer_strok):
    fraza = input()
    vse_frazi.append(fraza)

# 2. Считываем количество поисковых запросов
nomer_zaprosov = int(input())
vse_zaprosi = []

for j in range(nomer_zaprosov):
    zapros = input()
    vse_zaprosi.append(zapros)

# 3. Основная логика поиска
for fraza in vse_frazi:
    # Создаем "флажок", который изначально верит, что фраза подходит
    podhodit = True
    
    # Проверяем каждый запрос из нашего списка запросов
    for zapros in vse_zaprosi:
        # Если хотя бы один запрос (в нижнем регистре) НЕ найден во фразе
        if zapros.lower() not in fraza.lower():
            podhodit = False
            break # Дальше этот список запросов для этой фразы можно не проверять
    
    # Если после проверки всех запросов флажок остался True — печатаем
    if podhodit:
        print(fraza)