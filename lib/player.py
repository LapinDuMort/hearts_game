class Player():

    def __init__(self):
        hand = []
        tricks = []
        self.hand = hand
        self.tricks = tricks

    def add_to_hand(self, card):
        self.hand.append(card)
    
    def is_first(self):
        for card in self.hand:
            if card == ('2', 'Clubs'):
                return True
