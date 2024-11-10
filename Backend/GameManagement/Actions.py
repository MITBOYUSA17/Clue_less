
from abc import ABC, abstractmethod

import Backend
from Backend.GameManagement.player import Player
from Backend.GameManagement.player_turn import Player_Turn
from Backend.GameManagement.space import space

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

    def validate(self):
        if self.pt.hasMadeAccusation:
            return False
        else:
            return True

    def perform_action(self):
        # enter checking win conditions
        winningCards_iter = iter(list(Backend.GameManagement.GameProcessor.winningCards))
        nextCard = next(winningCards_iter)

        # output to GUI/client list of options for suspect, have them choose one

        self.suspect = selected_suspect

        # output to GUI/client list of options for weapon, have them choose one

        self.weapon = selected_weapon

        # output to GUI/client list of options for room, have them choose one

        self.room = selected_room

        suspectCorrect = False
        weaponCorrect = False
        roomCorrect = False
        if (nextCard.getCardType() == Suspect):
            if self.suspect == nextCard.getCardName():
                suspectCorrect = True
        else if nextCard.getCardType() == Weapon:
            if self.weapon == nextCard.getCardName():
                weaponCorrect = True
        else if nextCard.getCardType() == Room:
            if self.room = nextCard.getCardName():
                roomCorrect = True

        if (suspectCorrect and weaponCorrect and roomCorrect):
            # player wins game, enter win game state
        else:
            # output player eliminated
            p.isEliminated = True

class Suggestion(Actions):
    suspect: str
    weapon: str
    room: str

    def validate(self):
        if self.pt.hasEnteredRoom:
            if not self.pt.hasMadeAccusation:
                return True
        return False

    def perform_action(self):
        disproveFinished = False

        turnList = Backend.GameManagement.GameProcessor.turnOrder
        turnList_iter = iter(turnList)
        nextPlayer = None
        while (nextPlayer != p):
            nextPlayer = next(turnList_iter)

        while(not disproveFinished):
            nextPlayer = next(turnList_iter)
            # ask player to disprove
            # output list of player's cards that match suggestion
            # have them select one


    def create_suggestion(self, suspect: str, weap: str, room_suggest: str):
        # output to GUI/client list of options for suspect, have them choose one

        self.suspect = selected_suspect

        # output to GUI/client list of options for weapon, have them choose one

        self.weapon = selected_weapon

        # output to GUI/client list of options for room, have them choose one

        self.room = selected_room


class Move(Actions):
    Space destination
    Space currPos

    def validate(self):
        if self.p.get_valid_moves():
            return True
        return False

    def perform_action(self):
        moves_list = self.p.get_valid_moves()

        # output possible moves
        # have player select a move




