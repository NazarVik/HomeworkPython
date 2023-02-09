# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
def sum(a, b):
    if b == 0:
        if a == 0:
            return 0
        return sum(a - 1, b) + 1
    return sum(a, b - 1) + 1


num1 = int(input("enter number 1 = "))
num2 = int(input("enter number 2 = "))
print(sum(num1, num2))