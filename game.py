import random
option = ("rock","paper","scissor")
playing = True
while playing:
   
    player = None
    computer = random.choice(option)
    while player not in option:
        player = input ("enter a choice(rock,paper or scissor)")

    print(f"player:{player}")
    print(f"computer:{computer}")

    if player==computer:
        print("it is a tie")
    elif player=="rock" and computer=="paper":
        print("You Lost!")
    elif player=="scissor" and computer=="paper":
        print("You Won!")
    elif player=="rock" and computer=="scissor":
        print("You Won!")
    else:
        print("You Lost!")
    play_again = input("do you want to play again(yes/no)").lower()
    
    if not play_again=="yes":
        playing = False
        
print("Thanks for Playing")