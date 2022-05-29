import random
import time
from game_extras import board
from rules_to_win import rules_to_win
from game_extras import banner

# banner = banner()
# board = board()

def game(player_choice, comp_choice, player_score, computer_score, tie_score):
    spaces = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
    # Creating a list that stores the location which are empty
    # initializing it with all positions available
    remains = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # count variable to keep count of number of turns in the game
    count = 1
    flag = 0
    input("Press enter button to start ")
    print("\nTOSS happening...(1 for you, 0 against you)")
    time.sleep(1)
    while count <= 9:
        if count == 1:
            toss = random.randint(0,1)
            print(f"TOSS result: {toss}\n")
            time.sleep(0.75)
            if toss == 1:
                number = input(f"turn#{count}: Choose a number: ")
                number = int(number)
                # Removing the occupied position from 'remains' list
                remains.remove(number)
                # Updating the position occupied in the spaces dictionary created above
                spaces[number] = player_choice
                flag = 1
                count += 1
                # printing the board after each move to keep a track of occupied positions and those which are empty
                board.print_board(spaces)
                continue
            else:
                print(f"turn#{count}: Comp\'s turn to choose...")
                time.sleep(0.75)
                # Comp randomly selecting any position among the unoccupied positions
                number = random.choice(remains)
                print(f"     ...Comp chose {number}")
                remains.remove(number)
                spaces[number] = comp_choice
                count += 1
                board.print_board(spaces)
                continue
        
        if flag == 1:
            if count%2 == 0:
                print(f"turn#{count}: Comp\'s turn to choose...")
                time.sleep(0.75)
                number = random.choice(remains)
                if number not in remains:
                    print("\nOops! Try choosing a different number\n")
                    continue
                print(f"        Comp chose {number}")
                remains.remove(number)
                spaces[number] = comp_choice
                count += 1
                board.print_board(spaces)
            else:
                number = input(f"turn#{count}: Choose a number: ")
                number = int(number)
                if number not in remains:
                    print("\nOops! Try choosing a different number\n")
                    continue
                remains.remove(number)
                spaces[number] = player_choice
                count += 1
                board.print_board(spaces)
        
        else:
            if count%2 == 0:
                number = input(f"turn#{count}: Choose a number: ")
                number = int(number)
                if number not in remains:
                    print("\nOops! Try choosing a different number\n")
                    continue
                remains.remove(number)
                spaces[number] = player_choice
                count += 1
                board.print_board(spaces)
            else:
                print(f"turn#{count}: Comp\'s turn to choose...")
                time.sleep(0.75)
                number = random.choice(remains)
                if number not in remains:
                    print("\nOops! Try choosing a different number\n")
                    continue
                print(f"        Comp chose {number}")
                remains.remove(number)
                spaces[number] = comp_choice
                count += 1
                board.print_board(spaces)
        
        # game_end variable to indicate whether any player won, or is it a tie?
        game_end, player_score, computer_score= rules_to_win(spaces, player_choice, comp_choice, player_score, computer_score)
        # if game is won by any player, then terminate the loop
        if game_end:
            break

    # If count exceeds 9 and game isn't won by any player;
    # then definitely it's a tie!
    if count > 9 and (not game_end):
        tie_score += 1
        banner.banner_tie()

    answer = input('Do you want to play again?(y/n): ')

    return answer, player_score, computer_score, tie_score