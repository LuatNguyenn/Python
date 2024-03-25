import money_machine
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def makePayment(totalPayment):
    money_cal = MoneyMachine()
    is_paid = money_cal.make_payment(totalPayment)
    print("is_paid: ", is_paid)


def askToPay(coffee_choice):

    is_sufficient = coffee_maker.is_resource_sufficient(coffee_choice)

    if is_sufficient:
        total = money_machine.process_coins()
        paid = money_machine.make_payment(total)

        if paid:
            coffee_maker.make_coffee(coffee_choice)
            print(money_machine.report())


def getChoice():
    isOn = True
    while isOn:
        coffee_choice = str(input("What would you like (" + menu.get_items() + " ?\n"))

        if coffee_choice == "off":
            isOn = False
        elif coffee_choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            found = menu.find_drink(coffee_choice)
            if found.name == coffee_choice:
                askToPay(found)


getChoice()
