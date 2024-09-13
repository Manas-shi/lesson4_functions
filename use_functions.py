"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""

user_purchases = {}
user_account = 0
def account_replenishment():
    global user_account
    while True:
        input_amount = input("Введите сумму, на которую хотите пополнить счет: ")
        if input_amount.isdigit():
            amount = int(input_amount)
            user_account += amount
            print(f"Ваш счет пополнен на сумму {amount}. На Вашем счету теперь {user_account} тг.")
            break
        else:
            print("Ошибка: введите корректную числовую сумму.")

def purchase():
    global user_account

    while True:
        input_price = input("Введите цену товара, который хотите купить: ")
        if input_price.isdigit():
            price = int(input_price)
            break
        else:
            print("Ошибка: введите корректную числовую сумму для цены.")
    if price > user_account:
        print(f"У Вас на счету недостаточно средств для покупки. На Вашем счету: {user_account} тг.")
        return

    goods = input("Введите название товара, который хотите купить: ")
    user_purchases[goods] = price
    user_account -= price
    print(f"Поздравляем Вы купили {goods}. На Вашем счету теперь {user_account} тг.")

def purchase_history():
    while True:
        print("Меню: ")
        print("1. Посмотреть все покупки.")
        print("2. Найти товар по названию.")
        print("3. Выйти из меню.")

        choice = input("Выберите пункт меню: ")
        if choice == '1':
            if not user_purchases:
                print("История покупок пуста.")
            else:
                for item, cost in user_purchases.items():
                    print(f"{item}: {cost}")
        elif choice == '2':
            user_input = input("Введите название товара: ")
            if user_input in user_purchases:
                print(f"{user_input}: {user_purchases[user_input]}")
            else:
                print(f"Товара с названием {user_input} нет в истории покупок.")
        elif choice == '3':
            break
        else:
            print('Неверный пункт меню. Введите снова.')

while True:
    print("Меню:")
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')



    choice = input('Выберите пункт меню: ')
    if choice == '1':
        account_replenishment()
    elif choice == '2':
        purchase()
    elif choice == '3':
        purchase_history()
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')

