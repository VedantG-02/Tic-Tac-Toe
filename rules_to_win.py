from game_extras import banner


def rules_to_win(dic, player_choice, comp_choice, player_score, computer_score):
    # Conditions are as follows
    if dic[1]==dic[2] and dic[2]==dic[3]:
        if dic[1] == player_choice:
            player_score += 1
            banner.banner_you()
            return 1, player_score, computer_score
        elif dic[1] == comp_choice:
            computer_score += 1
            banner.banner_comp()
            return 1, player_score, computer_score

    elif dic[4]==dic[5] and dic[5]==dic[6]:
        if dic[4] == player_choice:
            player_score += 1
            banner.banner_you()
            return 1, player_score, computer_score
        elif dic[4] == comp_choice:
            computer_score += 1
            banner.banner_comp()
            return 1, player_score, computer_score

    elif dic[7]==dic[8] and dic[8]==dic[9]:
        if dic[7] == player_choice:
            player_score += 1
            banner.banner_you()
            return 1, player_score, computer_score
        elif dic[7] == comp_choice:
            computer_score += 1
            banner.banner_comp()
            return 1, player_score, computer_score
    
    elif dic[1]==dic[4] and dic[4]==dic[7]:
        if dic[1] == player_choice:
            player_score += 1
            banner.banner_you()
            return 1, player_score, computer_score
        elif dic[1] == comp_choice:
            computer_score += 1
            banner.banner_comp()
            return 1, player_score, computer_score

    elif dic[2]==dic[5] and dic[5]==dic[8]:
        if dic[2] == player_choice:
            player_score += 1
            banner.banner_you()
            return 1, player_score, computer_score
        elif dic[2] == comp_choice:
            computer_score += 1
            banner.banner_comp()
            return 1, player_score, computer_score
    
    elif dic[3]==dic[6] and dic[6]==dic[9]:
        if dic[3] == player_choice:
            player_score += 1
            banner.banner_you()
            return 1, player_score, computer_score
        elif dic[3] == comp_choice:
            computer_score += 1
            banner.banner_comp()
            return 1, player_score, computer_score
    
    elif dic[1]==dic[5] and dic[5]==dic[9]:
        if dic[1] == player_choice:
            player_score += 1
            banner.banner_you()
            return 1, player_score, computer_score
        elif dic[1] == comp_choice:
            computer_score += 1
            banner.banner_comp()
            return 1, player_score, computer_score

    elif dic[3]==dic[5] and dic[5]==dic[7]:
        if dic[3] == player_choice:
            player_score += 1
            banner.banner_you()
            return 1, player_score, computer_score
        elif dic[3] == comp_choice:
            computer_score += 1
            banner.banner_comp()
            return 1, player_score, computer_score
    return 0, player_score, computer_score
