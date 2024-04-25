# -*- coding: utf-8 -*-
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Ошибка: деление на ноль!"
        return x / y

    def calculate(self):
        while True:
            print("Выберите операцию:")
            print("1. Сложение")
            print("2. Вычитание")
            print("3. Умножение")
            print("4. Деление")
            print("5. Выйти")

            choice = input("Введите номер операции (1/2/3/4/5): ")
            if choice == '5':
                print("Выход....")
                break

            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
            except ValueError:
                print("Неправильный ввод! Введите число")
                continue

            if choice == '1':
                print("Результат: ", self.add(num1, num2))
            elif choice == '2':
                print("Результат: ", self.subtract(num1, num2))
            elif choice == '3':
                print("Результат: ", self.multiply(num1, num2))
            elif choice == '4':
                print("Результат: ", self.divide(num1, num2))
            else:
                print("Неверный ввод")

calc = Calculator()
calc.calculate()