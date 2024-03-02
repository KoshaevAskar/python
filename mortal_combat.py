import random

class Fighter:
    def __init__(self, name:str, name_fatality:str):
        self.name = name
        self.power = random.randint(1, 5)
        self.hp = 100
        self.name_fat = name_fatality
        self.fat__switch = True

    def attack(self, attacked_fighter):
        if self.fat__switch:
            self.fatality(attacked_fighter)
            attacked_fighter.hp -= self.power
            print(f'{self.name} наносит {self.power} ед. урона персонажу {attacked_fighter.name}')
            self.harakiri()

    def say_info(self):
        print(f'У персонажа {self.name} {self.hp} ед здоровья, {self.power} единиц силы')



    def fatality(self, attacked_fighter):
        if self.hp < 15:
            damage = random.randint(0, attacked_fighter.hp)
        attacked_fighter.hp -= damage
        print(f'{self.name}  применяет суператаку {self.name_fat} {self.name} и наносит {damage} ед. урона персонажу {attacked_fighter.name}')
        self.fat__switch = False
    
    def harakiri(self):
        if self.hp < 5 and random.randint(1, 2)==1:
                print(f'{self.name} совершил харакири')
                self.hp = 0

fighter1 = Fighter("маратик в попке шарик", "Скорпионья суператака")
fighter2 = Fighter("Охладулькин", "Сосульки-Ударюльки")


fighters = [fighter1, fighter2,]
enemy1 = random.choice(fighters)
fighters.remove(enemy1)
enemy2 = random.choice(fighters)
fighters.append(enemy1)

print(f"{enemy1.name} VS {enemy2.name}")

while True:
    enemy1.attack(enemy2)
    enemy2.attack(enemy1)
    enemy1.say_info()
    enemy2.say_info()
    if enemy1.hp <= 0 and enemy2.hp <= 0:
        print('Ничья')
        break
    elif enemy2.hp <= 0:
        print(f'{enemy1.name} победил')
        break
