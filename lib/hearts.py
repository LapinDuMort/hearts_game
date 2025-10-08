#This will act as the 'Main' for this project

#Importing the information from the Deck and Player classes
from lib.deck import *
from lib.player import *
import time

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
    
    #Initialise an empty trick to track the current plays
        c_trick = []
        self.c_trick = c_trick

    #Initialise first player, a category granted to whomever holds the 2 of Clubs, or who has won the previous trick
        first_player = ""
        self.first_player = first_player



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

#Define a function that accepts the number of cards in a hand, allows a user to numerically pick one and will loop if an invalid choice is made.
    def card_select(self, cards):
        user_choice = None
        if cards == 0:
            print("Hand is empty! End of round!")
            return None
        
        while True:
            if user_choice == "h" or user_choice == "H":
                x = 1
                for i in self.player_1.hand:
                    print(f"{x}: {i[0]} of {i[1]}")
                    x += 1
            try:
                user_choice = input("Please select which number of card you would like to play: ")
                if int(user_choice) >= 1 and int(user_choice) <= cards:
                    return int(user_choice)
                else:
                    print("That doesn't seem to be a valid choice! Please select a number for a card in your hand, or type [H] to see which cards are available.")
            except:
                print("That doesn't seem to be a valid choice! Please select a number for a card in your hand, or type [H] to see which cards are available. ")
    
    # Define a trick function that by default returns the current cards played, and if fed a value, instead adds the card to the trick        
    def trick(self, card=""):
        if card == "":
            if self.c_trick == []:
                return "The trick is currently empty"
            else:
                return self.c_trick
            
        else:
            self.c_trick.append(card)
            print(self.c_trick)
    #Define a function to check if the trick reaches four items, if it does, it will add them to the player's tricks and clear the trick
    def trick_check(self):
        if len(self.c_trick) == 4:
            print("Trick completed!")
            self.player_1.tricks.append(self.c_trick)
            self.c_trick = []
            print(f"Your current completed tricks are {self.player_1.tricks}")

    # Define bot play. Currently they just play out index 0. Time module pauses a second after each play to not overwhelm terminal
    def bot_play(self, player):
        #Player 2 selects the card at index 0
        if player == 2:
            v1 = self.player_2.hand.pop(0)
            print(f"Player Two selects {v1}")
            self.trick(v1)
            self.trick_check()
            time.sleep(1)
        #Player 3 selects the card at index 0
        elif player == 3:
            v2 = self.player_3.hand.pop(0)
            print(f"Player Three selects {v2}")
            self.trick(v2)
            self.trick_check()
            time.sleep(1)
        #Player 4 selects the card at index 0
        elif player == 4:
            v3 = self.player_4.hand.pop(0)
            print(f"Player Four selects {v3}")
            self.trick(v3)
            self.trick_check()
            time.sleep(1)

    def player_play(self):
        selection = self.card_select(x-1)
        try:
            self.trick(self.player_1.hand.pop(selection-1))
        except:
            quit()
        time.sleep(1)

    def play_order(self, player):
        x = player
        if x == 1:
            self.player_play()
        elif x != 1:
            self.bot_play(x)

    #Gameplay loop! Shows your hand, the current trick, and triggers card selection as well as the bot card selection
    def hand_start(self):
        print("Your hand contains: ")
        x = 1
        for i in self.player_1.hand:
            print(f"{x}: {i[0]} of {i[1]}")
            x += 1
        print("The current trick contains:")
        print(self.trick())
        self.trick_check()
        self.play_order(self.first_player)
        self.player_play()
        self.bot_play()

#Initial Gameplay Loop
def main():
    print("Welcome, Player!")
    print("New Game beginning, get ready!")
    hearts = Hearts()
    hearts.deal_opening_hands()
    while True:
        hearts.hand_start()