from Card import Card, CardType
from random import shuffle

class Hand():
    """
    Hand: Representative a collection of Cards

    This class provides methods for the management of a hand of cards. It provides
    operations for shuffling, dealing, adding, and removing cards.

    Attributes:
        cards (List: Card): List of Cards in the hand
    """
    def __init__(self):
        # Initialize Hand with an empty list of cards
        self._cards = []

    def add_card(self, card: Card):
        """Add a card to the hand."""
        if isinstance(card, Card):
            self._cards.append(card)
        else:
            raise ValueError("Must add an instance of Card.")

    def remove_card(self, card: Card):
        """Remove a card from the hand."""
        if card in self._cards:
            self._cards.remove(card)
        else:
            raise ValueError("Card not found in the hand.")

    def get_deck(self) -> list:
        """Return the current state of the hand."""
        return self._cards

    def clear_hand(self):
        """Clear all cards from the hand."""
        self._cards.clear()

    def has_card(self, card: Card):
        """Check if a specific card is in hand."""
        return card in self._cards

    def sort_hand(self):
        """Sort the cards in hand."""
        self._cards.sort()

    def display_hand(self):
        """Display the cards in hand."""
        return ', '.join(str(card) for card in self._cards)
# Sample
if __name__ == "__main__":
    hand = Hand()

    # Create some cards
    card1 = Card("Jamar", CardType.SUSPECT)
    card2 = Card("Kitchen", CardType.ROOM)
    card3 = Card("Golden Caribbean Macheté", CardType.WEAPON)

    # Add cards to the hand
    hand.add_card(card1)
    hand.add_card(card2)
    hand.add_card(card3)

    # Display the hand
    print("Hand before shuffling:", hand.get_deck())

    # Shuffle the hand
    hand.shuffle()
    print("Hand after shuffling:", hand.get_deck())

    # Deal a card
    dealt_card = hand.deal()
    print("Dealt card:", dealt_card)

    # Display the hand after dealing
    print("Hand after dealing a card:", hand.get_deck())

    # Remove a card
    hand.remove_card(card2)
    print("Hand after removing a card:", hand.get_deck())