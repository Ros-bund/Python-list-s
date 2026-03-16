# Считываем входную строку
nomer_vhod = input().split('-')

# Создаем список длин групп для обоих форматов без семерки и с семеркой
format_1 = [3, 3, 4]
format_2 = [1, 3, 3, 4]

# Сначала проверяем, что все части номера состоят только из цифр
vse_cifry = True
for chast in nomer_vhod:
    if not chast.isdigit():
        vse_cifry = False
        break

# Получаем длины каждой группы в текущем вводе
tekushie_dliny = [len(chast) for chast in nomer_vhod]

# Проверяем условия:
# 1. Все ли части — цифры
# 2. Соответствует ли список длин одному из шаблонов
# 3. Если это длинный формат, начинается ли он именно с '7'
if vse_cifry:
    if tekushie_dliny == format_1:
        print("YES")
    elif tekushie_dliny == format_2 and nomer_vhod[0] == '7':
        print("YES")
    else:
        print("NO")
else:
    print("NO")