# Считываем количество чисел
nomerov = int(input())

# Создаем список для хранения всех чисел
spisok_chisel = []

# Заполняем список числами из ввода
for i in range(nomerov):
    znachenie = int(input())
    spisok_chisel.append(znachenie)

# Находим самое маленькое и самое большое число в списке
samoe_malenkoe = min(spisok_chisel)
samoe_bolshoe = max(spisok_chisel)

# Проходим по списку и выводим числа, если они не равны минимуму или максимуму
for element in spisok_chisel:
    if element != samoe_malenkoe and element != samoe_bolshoe:
        print(element)