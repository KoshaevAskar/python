print("это приложение список желаний")
name = input("как к вам можно оброщаться:")
wishlist= []

while True:
    print(f"меню:") 
    print("1 - добавить желание")
    print("2 - показать все желания")
    print("3 - удалить желание ")
    action =input(f"что вы хотите сделать, {name}->") 
    if action =="1":
        wish  = input(f"{name}, какое желание вы хотите ввести:")
        if wish not in wishlist:
            wishlist.append(wish)
        
        elif action == "2":
            for i, wish in enumerate(wishlist, start = 1):
                print(f"{i}. {wish}")
        input("нажмите Enter, чтобы продолжить")
    elif action ==3:
        for i, wish in enumerate(wishlist, start = 1):
            print(f"{i}. {wish}")
        delete_index = input (f"{name}, введите номер желания для удаления:")
        delete_index = int(delete_index)
        delete_index = int (delete_index) - 1
        delete_wish = wishlist.pop(delete_index)
    input("нажмите Enter, чтобы продолжить")
    