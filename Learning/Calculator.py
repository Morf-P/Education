num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))

operation = input("Выберите операцию(+, -, *, /): ")

if operation == '+':
    operation = num_1 + num_2
elif operation == '-':
    operation = num_1 - num_2
elif operation == '*':
    operation = num_1 * num_2
elif operation == '/':
    operation = num_1 / num_2
else:
    print("Вы выбрали неправильную операцию, повторите попытку.")

print(operation)
