#This will act as the 'Main' for this project

#Importing the information from the Deck and Player classes
from lib.deck import *
from lib.player import *
from lib.hearts import *

#Initial Gameplay Loop
def main():
    print("Welcome, Player!")
    print("New Game beginning, get ready!")
    hearts = Hearts()
    hearts.deal_opening_hands()
    hearts.find_first_player()
    while True:
        hearts.hand_start()
main()
