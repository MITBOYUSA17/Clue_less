import pytest
from Card import Card, CardType
from Deck import Deck

def test_initial_deck_is_empty():
    deck = Deck()
    assert len(deck.get_deck()) == 0

def test_add_card_to_deck():
    deck = Deck()
    card = Card("Colonel Liburd", CardType.SUSPECT)
    deck.add_card(card)
    assert len(deck.get_deck()) == 1
    assert deck.get_deck()[0] == card

def test_remove_card_from_deck():
    deck = Deck()
    card = Card("Colonel Mustard", CardType.SUSPECT)
    deck.add_card(card)
    deck.remove_card(card)
    assert len(deck.get_deck()) == 0

def test_remove_nonexistent_card():
    deck = Deck()
    card1 = Card("Colonel Mustard", CardType.SUSPECT)
    card2 = Card("Club", CardType.ROOM)
    deck.add_card(card1)
    with pytest.raises(ValueError, match="Card not found in the deck."):
        deck.remove_card(card2)  # Attempt to remove a card that isn't in the deck

def test_shuffle_deck():
    deck = Deck()
    card1 = Card("Colonel Mustard", CardType.SUSPECT)
    card2 = Card("Library", CardType.ROOM)
    card3 = Card("Golden Caribbean Macheté", CardType.WEAPON)
    deck.add_card(card1)
    deck.add_card(card2)
    deck.add_card(card3)

    original_order = deck.get_deck()
    print(original_order)
    deck.shuffle()
    print(deck.get_deck())
    assert len(deck.get_deck()) == 3
    # Check that the cards are still the same but may be in a different order
    assert deck.get_deck() == original_order

def test_deal_card():
    deck = Deck()
    card = Card("Colonel Mustard", CardType.SUSPECT)
    deck.add_card(card)
    dealt_card = deck.deal()
    assert dealt_card == card
    assert len(deck.get_deck()) == 0  # Deck should be empty after dealing the only card

def test_deal_card_empty_deck():
    deck = Deck()
    assert deck.deal() is None  # Should return None when trying to deal from an empty deck
