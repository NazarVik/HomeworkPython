# Задача 4: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример 10: 1, 2, 3

n = int(input("введите число N = "))

for i in range(n):
    if 2**i <= n:
        print(i)
    else:
        break