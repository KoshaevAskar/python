import random
inventory = []
def gaw():
    print("гав-гав-гав!")
    global steps
    steps +=1
def robot_formard():
    print("робот идет вперед")

    
    
def robot_backward():
    print("робот идет назад")
    

def robot_right():
    print("робот идет на право")  
    

def robot_left():
    print("робот идет на лево")          

def robot_scan():
    global inventory
    items = ["Ветка,железо, алмаз,реактор"]
    item = random.choice(items)
    item = "Ветка"
    inventory.append(item)
    print(f"робот нашел предвет {item}")

def robot_pickup(item):
    global inventory
    inventory.append(item)

def  check_inventory():
    for index, item in enumerate(inventory, start=1):
        print(f"{index}. {item}")
def craft():
    recept1 = ["реактор", "железо"]# машина
    recept2 = ["реактор", "железо","алмазы"]# алмазная машина
    recept3 = ["реактор", "железо","алмазы","ветка"]# вертолет 
    recepts = [recept1, recept2, recept3]
    recept_names = ['Машина','Алмазная машина','Вертолет']
    print("Доступны новые рецепты:")
    for index, item in enumerate(recept_names, start=1):
        print(f"{index}. {item}")
    choice = input('Выбери,что хочешь крафтить: ')
    if not choice.isdigit():
        print("Вводить можно только числа")
        return None #выход из функции
    choice = int(choice) -1 # получаем нужный индекс
    if choice not in range(0,len(recept_names)-1):#если  выбрали не в диапазоне
        print("Рецепта с таким номером нет")
        return None
    choice_recept = recept_names[choice]
    print(f"вы выбрали крафтить {choice_recept}")
    ingrediens = recepts[choice]
    print(f"ингредиенты:{ingrediens}")
    for item in inventory:
        if item in inventory:
            print(f"уничтожен {item}")
            inventory.remove(item)
            ingrediens.remove(item)
            if not ingrediens:
                inventory.append(choice_recept)
                print(f"В инвентарь добавлен{choice_recept}")
                print("не хватает ингредиентов")
                                 

    while True:
        key = input("введите клавишу:")
        if key =="w":
            robot_formard()
        elif key == "s":
            robot_backward()
        elif key == "a":
            robot_left()
        elif key == "d":
            robot_right()
        elif key == "f":
        item = robot_scan()
        robot_pickup(item) 
        elif key =="e":
            check_inventory() 
        elif key =="c":
            craft()