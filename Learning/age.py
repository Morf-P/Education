age_sel = int(input("Введите ваш действительный возраст: "))

if age_sel <= 13:
    print(f"В {age_sel} лет, вы принадлежите к возрастной категории детей.")
elif 13 < age_sel <= 17:
    print(f"В {age_sel} лет, вы принадлежите к возрастной категории подростков.")
elif 17 < age_sel <= 59:
    print(f"В {age_sel} лет, вы принадлежите к возрастной категории взрослых.")
elif 59 < age_sel <= 120:
    print(f"В {age_sel} лет, вы принадлежите к возрастной категории стариков.")
else:
    print("Вы не ввели действительный возраст")
