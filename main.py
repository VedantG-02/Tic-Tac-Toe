from game import game
from game_extras import instructions
from scores import scores

name = input('Enter Username: ')

choices = ['O', 'X']
choice_copy = choices.copy()
player_choice = input('Choose among (X/O): ')
choice_copy.remove(player_choice.upper())
comp_choice = choice_copy[0]

# Initializing scores
player_score = 0
computer_score = 0
tie_score = 0

if __name__=='__main__':
    answers = ['y', 'yes', 'yeah', '1']
    answer = 'y'
    instructions()
    while(answer in answers):
        answer, player_score, computer_score, tie_score = game(player_choice, comp_choice, player_score, computer_score, tie_score)
    scores(name, player_score, computer_score, tie_score)