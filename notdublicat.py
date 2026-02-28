n = int(input())
seen = set()
result = []

for _ in range(n):
    s = input()
    # Проверяем, была ли уже такая строка в нашем множестве
    if s not in seen:
        result.append(s)   # Добавляем в список для сохранения порядка
        seen.add(s)        # Добавляем в "базу данных" увиденных строк

# Выводим результат построчно
for s in result:
    print(s)