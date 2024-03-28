grade_usr = int(input("Введите полученные баллы по предмету: "))

if grade_usr <= 20:
    grade_usr = str(grade_usr)
    print(f"{grade_usr} данные балы неудовлетворительные.")
elif grade_usr in range(21, 40):
    grade_usr = str(grade_usr)
    print(f"{grade_usr} данные балы удовлетворительные.")
elif grade_usr in range(41, 80):
    grade_usr = str(grade_usr)
    print(f"{grade_usr} данные балы хороши.")
elif 81 <= grade_usr < 101:
    grade_usr = str(grade_usr)
    print(f"{grade_usr} данные балы отличны.")
else:
    print("Ты что то напутал🤨")