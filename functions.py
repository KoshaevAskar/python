import random
inventory = []
def gaw():
    print("гав-гав-гав!")

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
    items = ["Ветка,железо"]
    item = random.choice(items)
    item = "Ветка"
    inventory.append(item)
    print(f"робот нашел предвет {item}")

def robot_pickup(item):
    global inventory
    inventory.append(item)


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
       robot_pickup("item")
       print(inventory)







