# May want to hide the data
class gameProcessor():
    def __init__(self):
        self.round_counter = 0
        self.turn_order = []
        self.state = 
        





class gameProcessor():
    def __init__(self):
        self.server_ip = ""
        self.server_port = 0
        self.game_id = ""
        self.round_counter = 0
        self.turn_order = None
        self.current_player = None
        self.game_board = None
        #self.character_deck = None
        #self.weapon_deck = None
        #self.room_deck = None



    
    def getTurnOrder(self):
        pass

    def setTurnOrder(self):
        pass

    def setRandomTurnOrder(self):
        pass

    def reverseTurnOrder(self):
        self.turn_order.reverse()

    def getCurrentPlayer(self):
        return self.current_player

    def getRoundCounter(self) -> int:
        return self.round_counter

    def setRoundCounter(self, round_counter: int):
        self.round_counter = round_counter


    def getWinningCard(self):
        pass

    def getGameBoard(self):
        pass

    def getCharacterDeck(self):
        pass

    def getWeaponDeck(self):
        pass

    def getRoomDeck(self):
        pass

    def getCharacters(self):
        pass

    def getWeapons(self):
        pass

    def getRooms(self):
        pass

    def getGameStatus(self):
        pass

    def setGameStatus(self):
        pass

    def createSolutionCaseFile(self):
        pass


