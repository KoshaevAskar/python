salary = 6900
veg_sale = 0.7# 70 процентов
cucumbers = 90 
tomato = 150
strowberry = 385
#умножение на veg_sale - овощи со скидкой
cookie = 140 + 140 
buy = (cucumbers * 5 + tomato * 4 )  * veg_sale + cookie # его покупка
print (f'у таксиста Вани из {salary} после траты {buy} рублей осталось {salary-buy} рублей')
print(10//3)#полное число
print(10%3)#остаток числа
left = salary - buy
stok = 134.65
travel = 36
print(f'таксист Ваня сможет купить{left //stok} акций')
print (f'у таксиста Вани останется {int(left % stok)} рублей проезд стоит {travel} рублей')

number = int(input('Введите число:'))
first = number // 100

third = number % 10
second =  number // 10 %10
print(third + first + second )

