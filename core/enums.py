from enum import Enum

class Species(Enum):
    #Species = [STR, INT, DEX, DEC]
    HUMAN = (2, 1, 1, 2)
    ELF = (-2, 3, 4, 1)
    DWARF = (5, -2, -2, 2)
    DEMON = (3, 2, -5, 4)

    def __init__(self, strength: int, intelligence: int, dexterity: int, deception: int):
        self.strength = strength
        self.intelligence = intelligence
        self.dexterity = dexterity
        self.deception = deception
        