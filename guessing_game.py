import random

print('################ Guessing Game ################')

limit_up = 100
limit_down = 1
max_turns = 10
min_turns = 5

nbr_to_guess = random.randint(limit_down, limit_up)
turns_remaining = random.randint(min_turns, max_turns)

while turns_remaining :
    if turns_remaining == 1:
        print('This is your last chance!')
    else : 
        print(f'You have {turns_remaining} chances to find the correct number!')
    
    choice = int(input('Enter your choice : '))

    if choice == nbr_to_guess:
        print(f'Good Job, you guessed it!!! {choice}')
        break
    elif choice > nbr_to_guess:
        print('You guessed too HIGH')
    else :
        print('You guessed too LOW')
  
    turns_remaining -= 1


