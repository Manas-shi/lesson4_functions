"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""

# year = input('Ввведите год рождения А.С.Пушкина:')
# while year != '1799':
#     print("Не верно")
#     year = input('Ввведите год рождения А.С.Пушкина:')

# day = input('Ввведите день рождения Пушкин?')
# while day != '6':
#     print("Не верно")
#     day = input('В какой день июня родился Пушкин?')
# print('Верно')


def pushkin_birth_year(year):
    while True:
        user_input = int(input('Введите год рождения А.С.Пушкина: '))
        if user_input != year:
            print("Не верно")
        else:
            print("Вы ответили верно")
            return pushkin_birth_day(6)

def pushkin_birth_day(day):
    while True:
        user_input = int(input('В какой день июня родился Пушкин? '))
        if user_input != day:
            print("Не верно")
        else:
            print("Вы ответили верно")
            return


pushkin_birth_year(1799)