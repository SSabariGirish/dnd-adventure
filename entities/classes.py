from hero import Hero
from core.enums import Species
from core.weapons import Weapon
from core.armour import Armour

class Knight(Hero):

    def __init__(self, species: Species, name: str):
        super().__init__(species, name, Weapon.IRON_BROADSWORD, Armour.IRON_CHAINMAIL, 100)

    def set_stats(self):
        self.cur_health = self._max_health
        self.strength += 8
        self.intelligence += 3
        self.dexterity += 5
        self.deception += 4

class Rogue(Hero):

    def __init__(self, species: Species, name: str):
        super().__init__(species, name, Weapon.IRON_DAGGER, Armour.LEATHER_ARMOUR, 75)
    
    def set_stats(self):
        self.cur_health = self._max_health
        self.strength += 3
        self.intelligence += 4
        self.dexterity += 8
        self.deception += 5

class Mage(Hero):

    def __init__(self, species: Species, name: str):
        super().__init__(species, name, Weapon.APPRENTICE_STAFF, Armour.APPRENTICES_ROBES, 50)
    
    def set_stats(self):
        self.cur_health = self._max_health
        self.strength += 2
        self.intelligence += 10
        self.dexterity += 4
        self.deception += 4