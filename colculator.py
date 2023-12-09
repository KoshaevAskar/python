

def plus(x,y):
    a = int(x)+int (y)
    print(f"Ответ:")



def minus (x,y):
    a = int(x)-int (y)
    print(f"Ответ:")


def deleniye (x,y):
    a = int(x)/int (y)
    print(f"Ответ:")




def mul (x,y):
    a = int(x)*int (y)
    print(f"Ответ: ")

def input_number(input_prhase):
    x = input(input_prhase)
    if not   x.isdigit ():
        print("Вводить можно только числа")
        return input_number(input_prhase)
    return int(x)


while True: 
    print('Меню')
    print('1 - +')
    print('2 - -')
    print('3 - /')
    print('4 - *')
    x = input_number("Введите первое число")
    y = input_number("Введите второе  число")


































































