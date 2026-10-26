
from one import Pizza, Drink, ComboSet, Order
from two import CardPayment, CashPayment


pizza1 = Pizza("Маргарита", 500, "small")
pizza2 = Pizza("Пепперони", 700, "small")
pizza3 = Pizza("Пепперони большая", 700, "large")

drink1 = Drink("Кола", 150, False)
drink2 = Drink("компот", 120, False)
combo = ComboSet("Комбо-сет", [pizza1, drink1])
order = Order()


while True:
    print("\n===== РЕСТОРАН =====")
    print("1. Маргарита - 500 сом")
    print("2. Пепперони - 700 сом")
    print("3. Большая пепперони - 910 сом")
    print("4. Кола - 150 сом")
    print("5. Компот - 120 сом")
    print("6. Комбо-сет - скидка 15%")
    print("7. Посмотреть заказ")
    print("8. Оплатить и выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        order.addItem(pizza1)

    elif choice == "2":
        order.addItem(pizza2)

    elif choice == "3":
        order.addItem(pizza3)

    elif choice == "4":
        order.addItem(drink1)

    elif choice == "5":
        order.addItem(drink2)

    elif choice == "6":
        order.addItem(combo)

    elif choice == "7":
        order.showOrder()

    elif choice == "8":
        if order.getTotalCost() == 0:
            print("Сначала выберите блюда!")
            continue

        order.showOrder()

        print("\nСпособ оплаты:")
        print("1. Банковская карта")
        print("2. Наличные")

        payment_choice = input("Выберите способ оплаты: ")

        if payment_choice == "1":
            payment = CardPayment()
        elif payment_choice == "2":
            payment = CashPayment()
        else:
            print("Неверный выбор")
            continue

        success = payment.collectPayment(order.getTotalCost())

        if success:
            order.nextStep()
            order.showOrder()
            print("Спасибо за заказ!")
            break

    else:
        print("Такого пункта нет")
