# This file includes code for instruuctions, banners and board

class banner():
    def __init__(self):
        pass

    def banner_you(self):
        print("\n*******************")
        print("*     YOU WIN     *")
        print("*******************\n")

    def banner_comp(self):
        print("\n********************")
        print("*     COMP WIN     *")
        print("********************\n")

    def banner_tie(self):
        print("***************")
        print("*     TIE     *")
        print("***************\n")

    def banner_start(self):
        print("#####################################################")

    def banner_end(self):
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

banner = banner()

def instructions():
    banner.banner_start()
    print("Instructions -> \n")
    print("1. Board is as follows:\n")
    print("\t| 1 | 2 | 3 |")
    print("\t-------------")
    print("\t| 4 | 5 | 6 |")
    print("\t-------------")
    print("\t| 7 | 8 | 9 |\n")
    print("2. First turn (among 'you' and 'Comp') will be selected randomnly.")
    print("3. For your turn, you have to select a number from 1 to 9 (excluding the number which has been chosen) to mark against the box.")
    print("Now continue with the game!\n")
    banner.banner_start()

class board():
    def __init__(self):
        pass

    def print_board(spaces):
        '''
        |   |   |   |
        -------------
        |   |   |   |
        -------------
        |   |   |   |
        '''
        print(f"\n\t| {spaces[1]} | {spaces[2]} | {spaces[3]} |")
        print("\t-------------")
        print(f"\t| {spaces[4]} | {spaces[5]} | {spaces[6]} |")
        print("\t-------------")
        print(f"\t| {spaces[7]} | {spaces[8]} | {spaces[9]} |\n")
