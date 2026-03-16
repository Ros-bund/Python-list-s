# Читаем первую строку, разбиваем её на части и превращаем в список целых чисел
l_spisok = [int(i) for i in input().split()]

# Аналогично читаем вторую строку для списка M
m_spisok = [int(i) for i in input().split()]

# Создаем пустой список для хранения результатов суммы
summa_spisok = []

# Проходим по парам элементов из обоих списков одновременно
for l_element, m_element in zip(l_spisok, m_spisok):
    tekushaya_summa = l_element + m_element
    summa_spisok.append(tekushaya_summa)

# Выводим все элементы итогового списка через пробел
print(*summa_spisok)