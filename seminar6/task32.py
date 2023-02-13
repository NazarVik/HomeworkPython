# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
list1 = [7, 9, 17, 13, 15, 4, 3, 54, 23, 3, 2]
minNum = int(input("enter min number = "))
maxNum = int(input("enter max number = "))

print(*[i for i in range(len(list1)) if minNum <= list1[i] <= maxNum])
