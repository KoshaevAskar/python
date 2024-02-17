# class Phone:
#     def __init__(self,name:str,processor:str,camera:str,memory:str):
#         self.name = name
#         self.processor = processor
#         self. camera = camera
#         self.memory = memory
    
#     def make_photo  (self):
#         print(f"{self.name} делает фото")
#     def listen_music(self):
#         print(f"{self.name} слушает музикю")
#         phone1.listen_music
# phone1 = Phone ("Sony","Snapdragon",50,512)
# phone2 = Phone ("Iphone","M1",12,64)
# print(phone1.camera)
# phone1.make_photo()


class Human:
    def __init__(self, name,surname, age, wight,growth):
        self.name = name
        self.surname = surname
        self.age = age
        self.wight = wight
        self.growth = growth
    def happy_birhtday (self):
        print( f"{self.name}  с др тебя пупсеночек")



class PhraseDecoration:
    def decorate(self, phrase):
        line = '-' * (len(phrase)+4)
        print(line)
        print('|', phrase, '|')
        print(line)




text = PhraseDecoration()
text.decorate('Я люблю АКC')
class son(father):
    pass       
son = son("Роман", 18)


