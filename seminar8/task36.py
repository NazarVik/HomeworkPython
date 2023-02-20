#  Задача No49. Решение в группах
#  Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество,
#    номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

def input_data():
    with open("data.txt", "a") as f:
        for i in range(int(input("введите кол-во новых записей в справочник - "))):
            f.write(input("введите ФИО и номер телефона: ").upper())
            f.write("\n")


def read_data():
    with open("data.txt", "r") as f:
        print(f.read())


def find_data():
    with open("data.txt", "r") as f:
        find_feature = input("введите одну из характеристик для поиска - ").upper()
        flag = False
        for i in f.readlines():
            list_feature = i.split()
            if find_feature in list_feature:
                print(i, end="")
                flag = True
        if not flag:
            print("такой записи не найдено")


while 1:
    get_choice = (int(input("""введите 
        1 - для добавления записи, 
        2 - для вывода всего справочника, 
        3 - для поиска, 
        4 - для завершения работы """)))
    match get_choice:
        case 1:
            input_data()
        case 2:
            read_data()
        case 3:
            find_data()
        case _:
            break