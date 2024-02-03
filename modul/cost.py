from constant import *
from order import *

def show_cost():
    global user_pizza, user_cost
    print(f'Вы заказали следущие пиццы')
    for i,  pizza in enumerate(PIZZA):
        print(f'{i+1}.{pizza} - {COST [i]} рублей')
    print('Общая стоимость заказа: ')
    summa = sum(user_cost)
    print(summa)
    return summa