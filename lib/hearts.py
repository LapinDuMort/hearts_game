#This will act as the 'Main' for this project

#Importing the information from the Deck and Player classes
from deck import *
from player import *

class Hearts():
    def __init__(self):    
    #Shuffle up a new deck of cards!    
        new_deck = Deck()
        new_deck.shuffle()
        self.new_deck = new_deck

    #Initialise all four starting players
        self.player_1 = Player()
        self.player_2 = Player()
        self.player_3 = Player()
        self.player_4 = Player()


#Loops through the shuffled deck, dealing one card to each player until the deck is empty
    def deal_opening_hands(self):
        x = 1
        for i in range(len(self.new_deck.deck)):
            if x == 1: 
                self.player_1.hand.append(self.new_deck.deal())
            elif x == 2:
                self.player_2.hand.append(self.new_deck.deal())
            elif x == 3:
                self.player_3.hand.append(self.new_deck.deal())
            else:
                self.player_4.hand.append(self.new_deck.deal())
                x = 0
            x += 1
        self.player_1.hand.sort()

def main():
    print("Welcome, Player!")
    print("New Game beginning, get ready!")
    hearts = Hearts()
    hearts.deal_opening_hands()
    print(f"Your starting hand is {hearts.player_1.hand}")


main()