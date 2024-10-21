from django.test import TestCase
from django.contrib.auth.models import User
from .models import Game, Person, Weapon, RoomHallway, Player, Card, GameSession
# Create your tests here.
# Helper setup functions to avoid repetitive code
def create_user(username="testuser"):
    return User.objects.create_user(username=username)

def create_room(name="Hallway", is_room=True, can_guess=True):
    return RoomHallway.objects.create(name=name, is_room=is_room, can_guess=can_guess)

def create_card(card_type="person", value="Colonel Mustard"):
    return Card.objects.create(card_type=card_type, value=value)


class GameModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user1 = create_user()
        user2 = create_user(username="testuser2")
        game = Game.objects.create(name="Game1", state="{'status': 'in progress'}")
        game.players.set([user1, user2])

    def test_name(self):
        game = Game.objects.get(id=1)
        game_name = game.name
        self.assertEqual(game_name, "Game1")

    def test_players(self):
        game = Game.objects.get(id=1)
        player_count = game.players.count()
        self.assertEqual(player_count, 2)

    def test_state(self):
        game = Game.objects.get(id=1)
        game_state = game.state
        self.assertIn('in progress', game_state)


class PersonModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Person.objects.create(name="John Doe")

    def test_name(self):
        person = Person.objects.get(id=1)
        person_name = person.name
        self.assertEqual(person_name, "John Doe")


class WeaponModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        room = create_room(name="Library")
        Weapon.objects.create(name="Candlestick", in_room=room)

    def test_name(self):
        weapon = Weapon.objects.get(id=1)
        weapon_name = weapon.name
        self.assertEqual(weapon_name, "Candlestick")

    def test_in_room(self):
        weapon = Weapon.objects.get(id=1)
        room_name = weapon.in_room.name
        self.assertEqual(room_name, "Library")


class RoomHallwayModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        room1 = create_room(name="Study", is_room=True)
        room2 = create_room(name="Kitchen")
        room1.connections.add(room2)

    def test_is_room(self):
        room = RoomHallway.objects.get(name="Study")
        is_room_flag = room.is_room
        self.assertTrue(is_room_flag)

    def test_can_guess(self):
        room = RoomHallway.objects.get(name="Study")
        can_guess_flag = room.can_guess
        self.assertTrue(can_guess_flag)

    def test_connections(self):
        room1 = RoomHallway.objects.get(name="Study")
        room2 = RoomHallway.objects.get(name="Kitchen")
        connections = room1.connections.all()
        self.assertIn(room2, connections)


class PlayerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        room = create_room(name="Lounge")
        player = Player.objects.create(player_name="Player1", current_location=room)
        card = create_card()
        player.holding_cards.add(card)

    def test_player_name(self):
        player = Player.objects.get(player_name="Player1")
        player_name = player.player_name
        self.assertEqual(player_name, "Player1")

    def test_current_location(self):
        player = Player.objects.get(player_name="Player1")
        location_name = player.current_location.name
        self.assertEqual(location_name, "Lounge")

    def test_holding_cards(self):
        player = Player.objects.get(player_name="Player1")
        card_count = player.holding_cards.count()
        self.assertEqual(card_count, 1)


class CardModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Card.objects.create(card_type="weapon", value="Knife")

    def test_card_type(self):
        card = Card.objects.get(value="Knife")
        card_type = card.card_type
        self.assertEqual(card_type, "weapon")

    def test_card_value(self):
        card = Card.objects.get(card_type="weapon")
        card_value = card.value
        self.assertEqual(card_value, "Knife")


class GameSessionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        player1 = Player.objects.create(player_name="Player1")
        player2 = Player.objects.create(player_name="Player2")
        game_session = GameSession.objects.create(turn_counter=2, round_counter=1)
        game_session.players.set([player1, player2])

    def test_players(self):
        session = GameSession.objects.first()
        player_count = session.players.count()
        self.assertEqual(player_count, 2)

    def test_turn_counter(self):
        session = GameSession.objects.first()
        turn_counter = session.turn_counter
        self.assertEqual(turn_counter, 2)

    def test_round_counter(self):
        session = GameSession.objects.first()
        round_counter = session.round_counter
        self.assertEqual(round_counter, 1)