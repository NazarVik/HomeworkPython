# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X

list = []
n = int(input("введите кол-во элементов массива = "))

print("введите ", n, " целых чисел(а)")
for i in range(n):
    list.append(int(input()))

x = int(input("введите искомое число = "))
maxElement = max(list)
minElement = min(list)

if minElement <= x <= maxElement:
    listDif = [abs(x - i) for i in list]
    resultIndex = listDif.index(min(listDif))
    print(list[resultIndex])
else:
    print((minElement, maxElement)[x > maxElement])



