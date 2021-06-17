from datetime import datetime as date
from Library.DiscountCard import DiscountCard

card1 = DiscountCard()
try:
    exit = False
    while not exit:
        item = int(input('1.Card information\n2. Buy with discount card \n3. Discount information \n4. Level up discount information \n5.Exit\n'))
        if item == 1:
            print(f'\n\tCard number: {card1.number}\n\tDate of issue: {card1.date}\n')
        elif item == 2:
            cost = float(input('The cost of the product you want to buy: \t-->'))
            card1.transaction(cost)
        elif item == 3:
            card1.disc_info()
        elif item == 4:
            card1.disc_dif_info()
        elif item == 5:
            print('Bye!')
            exit = True
        else:
            print('Wrong menu item!!!')
except:
    print('Wrong data')
