# file = open("text.txt",mode ="w", encoding = "UTF-8")
# file.write("happy new year!\n")
# file.write("happy year!")
# file.close()
# file = open("text.txt",mode ="w", encoding = "UTF-8")
# file.write("pepa year!")
# file.close()

# with  open("text.txt",mode ="a", encoding = "UTF-8") as file:
#     file.write(" \n rest work")
# with  open("text.txt",mode ="r", encoding = "UTF-8") as file:
#     text = file.read()
#     print (text)
import random
def file_write500():
    with  open("text.txt",mode ="a", encoding = "UTF-8") as file:
        for i in range(1,501):
            file.write("Я буду заниматься занятиями от А")

def  get_one_word(filename):          
    with  open( filename, mode ="r", encoding = "UTF-8") as file:
        text = file.read().split("\n")
        return random.choice(text)
pril =  get_one_word("prils.txt")
name = get_one_word("animals.txt")
print(f" в племени тумба-юмба вас бы звали {pril} {name}")
    
