table = ['круглый', 'квадратный']
table = str(input("Введите тип стола: "))
name = str(input("Пожалуйста, Введите Ваше имя: "))
bron = []

if table == 'круглый':
    for i in range(1, 9):
        table_col = 4
        if i == 3:
            continue
        if i == 5:
            continue
        if i == 6:
            continue
        print(f"количество стульев за столом {i} = {table_col}")
        spisok = i

bron_stol = str(input("Вы хотите забронировать стол?: "))
if bron_stol == 'да':
    confirm_bron = int(input("Выберите стол из свободных мест: "))
    print(f"Вы забронировали {confirm_bron} столик :)")
    print(f"Пожалуйста, {name} ожидайте официанта, он Вас проводит до вашего столика")
elif bron_stol == 'нет':
    print(f"Пожалуйста, {name} проходите за свободный столик, который есть в списке далее.")
    print(f"Свободные столики {spisok}")
else:
    print(f"Пожалуйста, {name} подождите администратора.")