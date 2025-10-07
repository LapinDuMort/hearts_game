from lib.hearts import *

def test_deck_shuffle():
    new_deck = Deck()
    new_deck.shuffle()
    result = new_deck.deck
    assert len(result) == 52 and result[0] != ['A', 'Hearts']

def test_deal():
    hearts = Hearts()
    hearts.deal_opening_hands()
    result = hearts.player_1.hand
    assert len(result) == 13

def test_equal_hands():
    hearts = Hearts()
    hearts.deal_opening_hands()
    result_1 = hearts.player_2.hand
    result_2 = hearts.player_4.hand
    assert len(result_1) == len(result_2) and result_1 != result_2
