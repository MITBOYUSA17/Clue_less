
from abc import ABC, abstractmethod

import Backend
from Backend.GameManagement.player import Player
from Backend.GameManagement.player_turn import Player_Turn

class Actions():
    p: Player
    pt: Player_Turn
    all_characters = {"Miss Scarlet", "Colonel Mustard", "Professor Plum", "Mr. Green", "Mrs. Peacock", "Mrs. White"}
    all_weapons = {"Candlestick", "Dagger", "Revolver", "Lead Pipe", "Wrench", "Rope"}
    all_rooms = {"Hall", "Lounge", "Dining Room", "Kitchen", "Ballroom", "Conservatory", "Billiard Room", "Library", "Study"}

    def __init__(self, player: Player, playerTurn: Player_Turn):
        p = player
        pt = playerTurn

    @abstractmethod
    def validate(self):

    @abstractmethod
    def perform_action(self):


class Accusation(Actions):
    suspect: str
    weapon: str
    room: str

    def create_accusation(self, c: str, weap: str, rm: str):
        suspect = c
        weapon = weap
        room = rm

    def validate(self):
        if pt.hasMadeAccusation:
            return False
        else:
            if(suspect not in all_characters):
                return False
            if(weapon not in all_weapons):
                return False
            if room not in all_rooms:
                return False
        return True

    def perform_action(self):
        # enter checking win conditions
        winningCards_iter = iter(list(winningCards.getDeck()))
        nextCard = next(winningCards_iter)
        suspectCorrect = False
        weaponCorrect = False
        roomCorrect = False
        if (nextCard.getCardType() == Suspect):
            if suspect == nextCard.getCardName():
                suspectCorrect = True
        else if nextCard.getCardType() == Weapon:

        else if nextCard.getCardType() == Room:


class Suggestion(Actions):
    character: str
    weapon: str
    room: str

    def validate(self):

    def perform_action(self):
        turnList = Backend.GameManagement.GameProcessor.turnOrder
        turnList_iter = iter(turnList)
        nextPlayer = None
        while (nextPlayer != p):
            nextPlayer = next(turnList_iter)

        nextPlayer = next(turnList_iter)

        # ask player to disprove


    def create_suggestion(self, suspect: str, weap: str, room_suggest: str):
        character = suspect
        weapon = weap
        room = room_suggest


class Move(Actions):
    Space destination
    Space currPos

    def __init__(self, p: Player):
        currentPos = p.currLocation

    def validate(self):


    def perform_action(self):



