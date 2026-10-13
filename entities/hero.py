from core.enums import Species
from core.weapons import Weapon
from core.armour import Armour

class Hero:

    def __init__(self, species: Species, name: str, weapon: Weapon, armour: Armour, max_health: int):
        self._species = species
        self._name = name
        self._weapon = weapon
        self._armour = armour
        self._max_health = max_health

        #Base stats
        self.strength = species.strength
        self.intelligence = species.intelligence
        self.dexterity = species.dexterity
        self.deception = species.deception
        self.cur_health = 0
                        

    def set_stats(self):
        """A method that would be inherited by child classes to update stats based on their class"""
        pass

    def take_damage(self, damage: int) -> None:
        """Reduces cur_health by amount, capped at 0."""
        if damage < 0:
            raise ValueError("Invalid damage amount")
        self.cur_health -= damage
        self.cur_health = max(0, self.cur_health)

    def heal(self, heal_amt: int) -> None:
        if heal_amt <= 0:
            raise ValueError("Invalid heal amount")
        
        self.cur_health += heal_amt
        self.cur_health = min(self._max_health, self.cur_health)

    def is_alive(self) -> bool:
        return self.cur_health > 0

    def calculate_damage(self) -> int:
        """
        Returns raw damage output. 
        Will be overridden by child classes to use STR or INT respectively.
        """
        pass

    def attack(self, target): # 'target' will be another Entity/Hero
        """Calculates damage and applies it to the target's take_damage method."""
        pass

    def __str__(self) -> str:
        """Returns a formatted character sheet for the CLI."""
        pass

    