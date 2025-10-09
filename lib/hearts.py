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
    
    #Initialise Trick Suit and a Hearts Broken bool
        trick_suit = ""
        hearts_broken = False
        self.trick_suit = trick_suit
        self.hearts_broken = hearts_broken



#Loops through the shuffled deck, dealing one card to each player until the deck is empty
    def deal_opening_hands(self):
        x = 1
        for deal in range(len(self.new_deck.deck)):
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
        #Ugly sort function that sorts by suit, and then rank    
        self.player_1.hand.sort(key=lambda val: ((self.new_deck.sort_suit[val[1]]), self.new_deck.sort_rank[val[0]]))

#Define a function that accepts the number of cards in a hand, allows a user to numerically pick one and will loop if an invalid choice is made.
    def card_select_any(self, cards):
        user_choice = None
        if cards == 0:
            print("Hand is empty! End of round!")
            return None
        
        while True:
            try:
                user_choice = input("Please select which number of card you would like to play or type [H] to view valid plays: ")
                
                if user_choice == "h" or user_choice == "H":
                    x = 1
                    for card in self.player_1.hand:
                        print(f"{x}: {card[0]} of {card[1]}")
                        x += 1
                
                elif int(user_choice) >= 1 and int(user_choice) <= cards:
                    return int(user_choice)
                else:
                    print("That doesn't seem to be a valid choice! Please select a number for a card in your hand, or type [H] to see which cards are available.")
            except:
                print("That doesn't seem to be a valid choice! Please select a number for a card in your hand, or type [H] to see which cards are available. ")
    
    # Define a function that works like card_select_any but ONLY allows a choice of cards from the valid trick suit
    def card_select_suit(self, cards, valid_cards):
        user_choice = None
        while True:
            try:
                user_choice = input("Please select which number of card you would like to play or type [H] to view valid plays: ")
                if user_choice == "h" or user_choice == "H":
                    x = 1
                    for card in valid_cards:
                        print(f"{x}: {card[0]} of {card[1]}")
                        x += 1
                    
                elif int(user_choice) >= 1 and int(user_choice) <= cards:
                    return valid_cards[int(user_choice) -1]
                else:
                    print("That doesn't seem to be a valid choice! Please select a number for a card in your hand, or type [H] to see which cards are available.")
            except:
                print("That doesn't seem to be a valid choice! Please select a number for a card in your hand, or type [H] to see which cards are available. ")
    
    # Passes a bot's hand to this function- if they may play any card they play the card at pos 0, otherwise, makes a valid list of cards in the suit, picks the first one, removes it from the hand and passes the value back
    def bot_select_card(self, hand):
        
        if len(hand) == 0:
            print("Hand is empty! End of round!")
            quit()
        if self.trick_suit == "":
            selected_card = hand.pop(0)
            return selected_card
        else:
            valid_cards = []
            cards_in_suit = False
            
            for card in hand:
                if card[1] == self.trick_suit:
                    cards_in_suit = True
                    valid_cards.append(card)

            if cards_in_suit == True:            
                selected_card = valid_cards.pop(0)
                hand.remove(selected_card)
                return selected_card
            
            else:
                selected_card = hand.pop(0)
                return selected_card

    
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
            self.trick_suit = ""
            self.c_trick = []
            print(f"Your current completed tricks are {self.player_1.tricks}")

    # Define bot play. Currently they just play out index 0. Time module pauses a second after each play to not overwhelm terminal
    def bot_play(self, player):
        #Player 2 selects the card at index 0
        if player == 2:
            v1 = self.bot_select_card(self.player_2.hand)
            print(f"Player Two selects {v1}")
            self.trick(v1)
            self.trick_check()
            time.sleep(1)
        #Player 3 selects the card at index 0
        elif player == 3:
            v2 = self.bot_select_card(self.player_3.hand)
            print(f"Player Three selects {v2}")
            self.trick(v2)
            self.trick_check()
            time.sleep(1)
        #Player 4 selects the card at index 0
        elif player == 4:
            v3 = self.bot_select_card(self.player_4.hand)
            print(f"Player Four selects {v3}")
            self.trick(v3)
            self.trick_check()
            time.sleep(1)

    # This function checks if the player can play any card because the trick is empty, or, if the trick is not empty, makes a list of valid cards they can choose from. If there are no valid cards in that suit, they can play any card.
    def player_play(self):
        cards_in_suit = False
        valid_cards = []
        if self.trick_suit == "":
            selection = self.card_select_any(len(self.player_1.hand))
            try:
                self.trick(self.player_1.hand.pop(selection-1))
                self.trick_check()
            except:
                quit()
            time.sleep(1)
        elif self.trick_suit != "":
            
            for card in self.player_1.hand:
                if card[1] == self.trick_suit:
                    cards_in_suit = True
                    valid_cards.append(card)

            if cards_in_suit == True:            
                selection = self.card_select_suit(len(valid_cards), valid_cards)
                self.player_1.hand.remove(selection)
                self.trick(selection)
                self.trick_check()
                time.sleep(1)
            
            else:
                selection = self.card_select_any(len(self.player_1.hand))
                try:
                    self.trick(self.player_1.hand.pop(selection-1))
                    self.trick_check()
                except:
                    quit()
                time.sleep(1)

    #Defines order of play. Checks who is the first player, then does one iteration to that goes 1 > 2 > 3 > 4 > 1
    #After the first card is played, sets the suit of the trick to that card.
    def play_order(self, player):
        x = player
        cards_played = 0

        while cards_played < 4:
            if cards_played == 1:
                self.trick_suit = self.c_trick[0][1]

            if x == 1:
                self.player_play()
                x += 1
                cards_played += 1
            elif x != 1:
                self.bot_play(x)
                if x == 4:
                    x = 1
                    cards_played += 1
                else:
                    x += 1
                    cards_played += 1

    #Gameplay loop! Shows your hand, the current trick, and triggers card selection as well as the bot card selection
    def hand_start(self):
        print("Your hand contains: ")
        x = 1
        for card in self.player_1.hand:
            print(f"{x}: {card[0]} of {card[1]}")
            x += 1
        print("The current trick contains:")
        print(self.trick())
        self.trick_check()
        self.play_order(self.first_player)

    #Checks each players hand and sets the person who holds the 2 of Clubs as the first player
    def find_first_player(self):
        for card in self.player_1.hand:
            if card == ['2', 'Clubs']:
                self.first_player = 1
        for card in self.player_2.hand:
            if card == ['2', 'Clubs']:
                self.first_player = 2
        for card in self.player_3.hand:
            if card == ['2', 'Clubs']:
                self.first_player = 3
        for card in self.player_4.hand:
            if card == ['2', 'Clubs']:
                self.first_player = 4


#Initial Gameplay Loop
def main():
    print("Welcome, Player!")
    print("New Game beginning, get ready!")
    hearts = Hearts()
    hearts.deal_opening_hands()
    hearts.find_first_player()
    while True:
        hearts.hand_start()
#main()