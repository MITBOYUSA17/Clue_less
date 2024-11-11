from enum import Enum, auto
from typing import List

class SpaceType(Enum):
    ROOM = auto()
    CORNER_ROOM = auto()
    HALLWAY = auto()
    def __str__(self) -> str:
        return self.name.replace("_",' ').title()

class Space():
    def __init__(self, name: str = ""):
        self.space_name: name
        self.space_type: SpaceType = None
        self.players: List[Player] = []
        self.adjacent_spaces: List[Space] = []
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other,Space):
            return False
        if self.space_type != other.space_type:
            return False
        if self.space_type == SpaceType.HALLWAY:
            return self.adjacent_spaces == other.adjacent_spaces
        
        return self.name == other.name
        
    
    def get_space_name(self) -> str:
        return self.space_name
    
    def set_space_name(self, name: str):
        self.space_name = name
    
    def get_space_type(self) -> SpaceType:
        return self.space_type
    
    def get_space_type_name(self) -> str:
        return str(self.space_type)
        
    def set_space_type(self, space_type: SpaceType):
        self.space_type = space_type
    
    def get_player_count(self) -> int:
        return self.players.count()
    
    
    def add_adjacent_space(self, space: Space):
        self.adjacent_spaces.append(space)

    
    def remove_adjacent_space(self,space: Space):
        self.adjacent_spaces.remove(space)

    def remove_adjacent_space(self,index: int):
        adjacent_spaces_len = len(self.adjacent_spaces)
        if index < adjacent_spaces_len and index >= 0:
            self.adjacent_spaces.remove(index)
    
    def get_adjacent_spaces():
        return self.adjacent_spaces
    

    def getAdjacentSpace(name: str):
        pass

    def removeAdjacentSpace(name: str):
        pass

    def getAdjacentSpaces():
        return self.adjacent_spaces

    def setAdjacentSpaces(spaces: List[Space]):
        self.adjacent_spaces = spaces

   
    def addPlayer():
        self.player_count + 1
    
    def setPlayer(players: List[Player]):
        pass

    def removePlayer() -> Player:
        pass

    def getPlayer():
        pass

    def 


class Room(Space):
    def __init__(self):
        self.secret_passages = []
        self.weapons = []
        self.setSpaceType(SpaceType.Room)
    
    def addSecretPassage(secret_passage: Hallway):
        pass

    def setSecretPassages(secrets: Hallway):
        pass

    def getSecretPassages():
        return self.secret_passages

    def isSecretPassage():
        if self.secret_passages:

    def addWeapon(weapon: Weapon):
        self.weapons.append(weapon)

    def removeWeapon(name: str) -> Weapon:
        pass

    def removeWeapon(index: int) -> Weapon:
        pass

    def setWeapons(weapons: List[Weapon]):
        self.weapons = weapons
        

class CornerRoom(Room):
    def __init__(self):

        self.setSpaceType(SpaceType.CornerRoom)

class Hallway(Space):

    def __init__(self):
        self.setSpaceType(SpaceType.Hallway)
        self.must_leave = False
        self.is_empty = True
    
    def isEmpty() -> bool:
        return self.is_empty

# maybe all it player must move
    def playerMustLeave() -> bool:
        return self.must_leave 

    def addPlayerToSpace():
        if self.isEmpty():
            pass
