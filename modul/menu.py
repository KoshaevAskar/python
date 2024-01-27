PIZZA = ['Маргарита','Пепперони','4 Сыра','Гавайская']
COST = [550,675, 700, 850]

user_pizza = []
user_cost = []

def choice_pizza():
    print('Добро пожаловать в пиццерию "PIZZA DERAM"!')
    print('Меню пиццерии:')
    for i,  pizza in enumerate(PIZZA):
        print(f'{i+1}.{pizza} - {COST{i}} рублей')
        while True:
            order = int(input('Выберите свою пиццу >>>'))
            user_pizza.append(PIZZA[order-1 ])
            user_cost.append(COST[order-1])
            print('Пицца добавлена в корзину!')
            flag = input('Хотите продолжить заказывать?')
            if flag.upper() == 'НЕТ':
                print('Вы вышли из меню')
                break
