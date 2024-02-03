from constant import *
from order import *


def choice_pizza():
    print('Добро пожаловать в пиццерию "PIZZA DERAM"!')
    print('Меню пиццерии:')
    for i,  pizza in enumerate(PIZZA):
        print(f'{i+1}.{pizza} - {COST [i]} рублей')
    while True:
        order = int(input('Выберите свою пиццу >>>'))
        order -=1
        get_order(order_pizza=order)
        print('Пицца добавлена в корзину!')
        flag = input('Хотите продолжить заказывать?')
        if flag.upper() == 'НЕТ':
             print('Вы вышли из меню')
             break
        

