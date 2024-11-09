

class Player():
    playerName: str
    playerID: int
    character: str
    playerHand: list
    currLocation: Space
    prevLocation: Space

    def __init__(self, name: str):
        playerName = name

    def receive_card_dealt(self, card: Card):
        playerHand.addCard(card)

    def get_valid_moves(self):
        # returns a list of Space objects
        adj = currLocation.adjacentSpaces
        returnList = []
        for Space s in adj:
            if s.isEmpty:
                returnList.append(s)

        return returnList


