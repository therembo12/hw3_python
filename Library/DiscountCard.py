import random
from datetime import datetime as date

class DiscountCard:

    def __init__(self):
        self.__number = random.randint(10000000, 99999999)
        self.__money = 0
        self.__disc = 1
        self.__date = date.now().strftime("%d-%m-%Y")

    def transaction(self, cost: float):
        if cost > 0:
            pay = cost - (cost * self.__disc / 100)
            print(
                f'Your discount  {cost * self.__disc / 100} UAH. To be paid {pay} UAH.')
            confirm = input("Do you want continue: Y/N --> ")
            if confirm.upper() == 'Y':
                self.__money += pay
                self.__disc = round(
                    self.__money // 1000 + 1) if round(self.__money // 1000 + 1) <= 15 else 15
                print("Transaction complite!\n")
            elif confirm.upper() == 'N':
                print("Bye!\n")
            else:
                print("Wrong command. Please try again.\n")
        else:
            print("Wrong price. Please try again.\n")

    def discount_info(self):
        print(
            f'Your discount {self.__disc}%.\n')

    def discount_dif_info(self):
        next_lev = self.__disc * 1000 - self.__money
        if next_lev == 0:
            next_lev = 1000
        print(
            f'Your discount {self.__disc}%. For more discount, you need to buy good more than {next_lev} UAH.\n')

    @property
    def number(self):
        return self.__number

    @property
    def money(self):
        return self.__money

    @property
    def disc(self):
        return self.__disc

    @property
    def date(self):
        return self.__date