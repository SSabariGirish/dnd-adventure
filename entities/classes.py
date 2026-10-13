from hero import Hero
from core.enums import Species
from core.weapons import Weapon

class Knight(Hero):

    def __init__(self, species: Species, name: str):

        super().__init__(species, name, weapon, armour, 100)