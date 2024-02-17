import random

class Fighter:
    def __init__(self , name:str, name_fatality:str):
        self.name = name
        self.power = random.randint(1, 5)
        self.hp = 100

fighter1 =  Fighter('скорпион','скорпионья суператака')
fighter2 = Fighter('охладулькин','сосульки')
fighter3 = Fighter('ПУПЕР СИГМА', 'Поднимает бровь вверх, и складывает губы  в трубочку')
fighter4 = Fighter('свинка пепа ', 'супер пердежь и рыг')
fighters = [fighter1, fighter2, fighter3, fighter4 ]
enemy1 = random.choice(fighters)
fighters.remove(enemy1)
enemy2 = random.choice(fighters)
fighters.append (enemy1)

print(f'{enemy1.name} VS {enemy2.name}')