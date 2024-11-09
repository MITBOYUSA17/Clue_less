import pytest
from Card import Card, CardType
from Hand import Hand

def test_initial_deck_is_empty():
    hand = Hand()
    assert len(hand.get_deck()) == 0

def test_add_card_to_deck():
    hand = Hand()
    card = Card("Colonel Liburd", CardType.SUSPECT)
    hand.add_card(card)
    assert len(hand.get_deck()) == 1
    assert hand.get_deck()[0] == card

def test_remove_card_from_deck():
    hand = Hand()
    card = Card("Colonel Mustard", CardType.SUSPECT)
    hand.add_card(card)
    hand.remove_card(card)
    assert len(hand.get_deck()) == 0

def test_remove_nonexistent_card():
    hand = Hand()
    card1 = Card("Colonel Mustard", CardType.SUSPECT)
    card2 = Card("Club", CardType.ROOM)
    hand.add_card(card1)
    with pytest.raises(ValueError, match="Card not found in the hand."):
        hand.remove_card(card2)  # Attempt to remove a card that isn't in the hand

def test_clear_hand():
    hand = Hand()
    card1 = Card("Colonel Mustard", CardType.SUSPECT)
    card2 = Card("Library", CardType.ROOM)
    card3 = Card("Golden Caribbean Macheté", CardType.WEAPON)
    hand.add_card(card1)
    hand.add_card(card2)
    hand.add_card(card3)
    hand.clear_hand()
    assert len(hand.get_deck()) == 0  # Hand should be empty after dealing the only card