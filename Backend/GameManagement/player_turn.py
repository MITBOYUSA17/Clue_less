
from Backend.GameManagement.Actions import Actions
from Backend.GameManagement.player import Player

class Player_Turn():
    p: Player
    hasMadeAccusation: bool

    def __init__(self, player: Player):
        p = player
        hasMadeAccusation = False

    def get_valid_actions(self):
        returnList = []
        if p.get_valid_moves():
            newMove = Move(p)
            returnList.append(new Move)

    def take_action(self, action: Actions):

    def end_turn(self):

