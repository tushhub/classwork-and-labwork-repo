import random

ran_num = random.randint(1, 10)
for i in range(1,4):
    user_num = int(input("Guess the Number (1 to 10): "))
    if ran_num == user_num:
        print("Your Guess Is Right.")
        break
    else:
        print("You lost the game")
        continue
print("Genratade Number: ",ran_num)
        
