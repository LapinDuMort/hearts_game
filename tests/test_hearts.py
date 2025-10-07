from lib.hearts import *

def test_deck_shuffle():
    new_deck = Deck()
    result = new_deck.shuffle()
    assert "9 Hearts" in result
