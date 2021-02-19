from exceptions import *

def player_live(live):
    if live == 1:
        print("You choose hard mode")
    elif live == 3:
        print("You choose middle mode")
    elif live == 5:
        print("You choose easy mode")
    else:
        raise IncorrectLivesInput
def rules():
    return ("\nRules: The game is an interpretation of the game stone paper scissors,\n"
          "but instead of the classic: stone scissors and paper, it is used: \n"
          "a wizard, a warrior and a robber who are meant by the numbers (1, 2, 3), respectively. \n"
          "The wizard defeats the warrior, the warrior defeats the rogue, and the rogue defeats the wizard.\n ")
