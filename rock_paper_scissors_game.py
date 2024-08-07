# rock paper scissors game
import random

def get_user_choice():
    user_choice = input(" CHOOSE (rock , paper or scissors): ").lower()
    while user_choice not in ["rock","paper","scissors"]:
        print("----Invalid---- \n Choose from Rock , Paper , Scissors ")
        user_choice=input(" CHOOSE (rock , paper or scissors): ").lower()
    return user_choice
    
def get_computer_choice():
    return random.choice(["rock","paper","scissors"])    

def winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif(user_choice == "rock" and computer_choice =="scissors") or \
        (user_choice == "scissors" and computer_choice =="paper") or \
        (user_choice == "paper" and computer_choice =="rock"):
       return "user"
    else:
        return "computer"
    
def play_game():
    user_score = 0
    computer_score = 0

    print("         --- WELCOME ---        ")
    print("---Rock Paper & Scissors Game---")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}   Computer chose {computer_choice}.")
    
        result = winner(user_choice,computer_choice)

        if result == "tie":
            print("---It's a Tie ---")
        elif result =="user":
            print("--- You Win ---")
            user_score += 1
        else:
            print("--- You Lose ---")
            computer_score += 1        

        print(f"Score : USER - {user_score}     COMPUTER - {computer_score}")

        quit_game = input("Type quit to end the game , or press enter to continue :").lower()
        if quit_game == "quit":
            break
       
    print("Final Score:")
    print(f"User: {user_score} - Computer: {computer_score}")
    print("Thanks for playing!")

    
play_game()    