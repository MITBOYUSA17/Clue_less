# tests/test_card.py
import pytest
from Card import CardType, Card

@pytest.fixture
def card():
    """Fixture to create a Card instance for testing."""
    return Card("Test Card", CardType.SUSPECT)

def test_card_initialization(card):
    """Test the initialization of the Card class."""
    assert card.get_name() == "Test Card"
    assert card.get_card_type() == CardType.SUSPECT

def test_set_name(card):
    """Test the set_name method."""
    card.set_name("New Card Name")
    assert card.get_name() == "New Card Name"

def test_set_card_type(card):
    """Test the set_card_type method with a valid CardType."""
    card.set_card_type(CardType.ROOM)
    assert card.get_card_type() == CardType.ROOM

def test_set_card_type_invalid(card):
    """Test the set_card_type method with an invalid type."""
    with pytest.raises(ValueError, match="card_type must be an instance of CardType Enum."):
        card.set_card_type("Invalid Type")  # Passing a string instead of CardType

def test_card_equality():
    """Test the equality operator."""
    card1 = Card("Fireball", CardType.WEAPON)
    card2 = Card("Fireball", CardType.WEAPON)
    card3 = Card("Shield", CardType.WEAPON)

    assert card1 == card2  # Same name and type
    assert card1 != card3  # Different name

def test_card_repr(card):
    """Test the __repr__ method."""
    assert repr(card) == "Card(name='Test Card', card_type=CardType.SUSPECT)"

def test_card_str(card):
    """Test the __str__ method."""
    assert str(card) == "name='Test Card', card_type=CardType.SUSPECT"