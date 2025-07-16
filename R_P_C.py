# rock_paper_sesior
# input: rock, paper, or sesior
# output: win, lose, or draw
import random


def play_game(user_choice):
    choice = ['rock','paper','sesior']
    computer_choice = random.choice(choice)
    print(f'Computer chose: {computer_choice}')


    if user_choice == computer_choice:
        return 'draw'
    
    elif(user_choice == 'rock' and computer_choice == 'sesior') or \
        (user_choice == 'paper' and computer_choice == 'rock') or \
        (user_choice == 'sesior' and computer_choice == 'paper'):
        return 'win'

    else:
        return 'lose'
    
def main():
    user_choice = input("Enter your choice (rock, paper, sessior):").lower()
    print(play_game(user_choice))



if __name__ == "__main__":
    main()
    




    
    







