from core.enums import Species

class Hero:

    def __init__(self, species: Species, name: str, weapon: str, armour: str):
        self._species = species
        self._name = name
        self._weapon = weapon
        self._armour = armour
    