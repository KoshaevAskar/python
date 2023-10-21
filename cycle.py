# counter = 1
# while counter <= 10:
#     print(counter)
#     counter += 1

# sandwich = 1 
# while sandwich<=30:
#     print(f"сделал {sandwich} -й бутерброд")
#     sandwich+=1
import time
number = 20 
summa = 0
while number > 9:
    print(number)
    summa += number
    time.sleep(1)
    print(f"Прибавили {number}, получилось {summa}")
    number -=1

rain = True 
while rain:
    print("я играю бс")
    stop = input ("Дождь кончился да/ нет")
    if stop == "да":
        print("ДОЖДЬ КОНЧИЛСЯ")
        break 
     