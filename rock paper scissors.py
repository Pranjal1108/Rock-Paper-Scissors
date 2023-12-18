choices = ["rock", "paper", "scissors"]
import random
while True:
    Ai_pick = random.choice(choices)
    Your_pick = str(input("Your pick: "))
    print("AI picked:", Ai_pick)
    if Your_pick == Ai_pick:
        print( "it's a draw ")
    elif(
        (Your_pick == "rock" and Ai_pick == "scissors") or
        (Your_pick == "paper" and Ai_pick == "rock") or
        (Your_pick == "scissors" and Ai_pick == "paper")
        ):
        print(" You Won ")
    else:
        print("You Lose")
        
    continuation = str(input(" do you want to continue ? "))
    if continuation != "yes":
        print("ok")
        break
 