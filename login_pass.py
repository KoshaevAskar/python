import calculator
inport functions
import wishlist








def sign_up():
    login = input("Придумайте логин: ")
    password1 = input('Придумайте пароль: ')
    password2 = input('Введите пароль еще раз: ')
    if password1 == password2:
        write_to_file('logins.txt', login + '\n')
        write_to_file('passwords.txt',password1 + '\n')
        print(f'Пользователь {login} успешно зарегистрирован')
    else:
        print('Пароли не схожи. Проверьте-ка еще раз')

def sign_in():
    login = input('введите логин:')
    password = input('введите пароль:')
    login_list = read_list('logins.txt')
    password_list = read_list ('passwords.txt')
    if login in  login_list:
        login_str = login_list.index(login)
        true_password = password_list[login_str]
        if password == true_password:
            print('вы успещно вошли в систему')
            return True
        else:
            print ("пароль не правельный")
            return False
    else:
        print("пользователя с таким логеном не найдено")
        return False

def write_to_file(filename, text):
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)


def read_list(filename):
    with open (filename, mode ='r', encoding='utf-8' ) as file:
        text = file.read().split('\n')
        return text 


access = False
while True:
    if not access:
        print('Это программа БоберКор, и вот что она умеет: ')
        print('1 - зарегистрироваться')
        print('2 - войти в систему')
        print('3 - выйти из программы')
        action = input('Введите номер действия: ')
        if action == '1':
            sign_up()
        elif action == '2':
            sign_in()
        if action == '3`':
            print('Спасибо за пользование программы')
            break
    elif access:
            print('меню:')
            print("1 - запустить калькулятор")
            print("2 - запустить текстокрафт")
            print("3 - запустить вишь лист")
            if action =="1":
                calculator.main()
            if action =="2":
                functions.main()
            if action =="3":
                wishlist.main()
                    

                

                
    input('Нажмите Enter, чтобы продолжить')
    







