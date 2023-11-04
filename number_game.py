import random
print("Это игра угадай число")
print("в этой игре комп напишет цифру а ты должен ее угодать от 1 до 100")
game_round = 0 
while game_round < 3:
    game_round+=1
    print(f"раунд №{game_round}") 
    attemts = 1
    number_in_game = random.randint(1,100) 
    while attemts < 10:
        our_number = input("введите числo: ")
        if not our_number.isdigit():
            print(f"вы ввели не число")
            continue
        attemts+=1
        our_number= int(our_number)

        print(f"вы ввели {our_number}")

        if our_number > number_in_game:
            print("Вы ввели больше,чем у меня")
        elif our_number < number_in_game:
            print("Вы ввели меньше, чем у миня")
        elif our_number == number_in_game:
            print("Ты угодал! молодец")
            break
        if attemts == 10:
            print("все попытки истрачены")
            break



