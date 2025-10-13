#Importing the random module to give us access to shuffling
import random
#Initialise a Deck of cards class to be called by the main branch of the program
class Deck():

    def __init__(self):
        suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
        ranks = ["A" , "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        deck = []
        for i in ranks:
            for j in suits:
                deck.append((i,j))
        self.deck = deck
    #Assign values for sorting/scoring hands
        sort_suit = {"Hearts":0, "Clubs":1, "Diamonds":2, "Spades":3}
        sort_rank = {"2":0, "3":1, "4":2, "5":3, "6":4, "7":5, "8":6, "9":7, "10":8, "J":9, "Q":10, "K":11, "A":12}
        self.sort_suit = sort_suit
        self.sort_rank = sort_rank

#Create Shuffle function to shuffle the deck
    def shuffle(self):
        random.shuffle(self.deck)
        

#Create deal function to take a card from the deck, remove it, and return it
    def deal(self):
        return self.deck.pop()        
