# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его
# кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются
# друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”,
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

example_string = "аяуюоеёэиы"
list_str = "пара-ра-рам-па рам-пам-папам па-ра-па-м".split()
list_len = []

for one_str in list_str:
    # list_vowels = [vowels for vowels in one_str if vowels in example_string]  # [a,a,a,a]
    list_vowels = list(filter(lambda x: x in example_string, one_str))
    list_len.append(len(list_vowels))

print("Парам пам-пам" if len(set(list_len)) == 1 else "Пам парам")



