# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в
# целую степень B с помощью рекурсии.

def exponentiation(x, y):
    if y == 0:
        return 1
    return exponentiation(x, y - 1) * x


a = int(input("add number = "))
b = int(input("add degree = "))
print(exponentiation(a, b))
