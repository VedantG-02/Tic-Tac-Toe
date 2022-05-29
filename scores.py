from game_extras import banner

# banner = banner()

def scores(name, player_score, computer_score, tie_score):
	banner.banner_end()
	print(f"SCORES -> {name}: {player_score}")
	print(f"          Comp: {computer_score}")
	print(f"          Tie: {tie_score}")
	banner.banner_end()
	print()