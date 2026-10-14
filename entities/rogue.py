from .hero import Hero
from core.enums import Species
from core.weapons import Weapon
from core.armour import Armour
import random

class Rogue(Hero):

    def __init__(self, species: Species, name: str):
        super().__init__(species, name, Weapon.IRON_DAGGER, Armour.LEATHER_ARMOUR, 75)
        self.set_stats()
    
    def set_stats(self):
        self.cur_health = self._max_health
        self.strength += 3
        self.intelligence += 4
        self.dexterity += 8
        self.deception += 5

    def take_damage(self, damage: int):
        dodge_chance = 0.25

        if random.random() <= dodge_chance:
            print(f"{self._name} dodged the attack!")
        else:
            damage = max(0, damage - self._armour.defence)
            super().take_damage(damage)

    def calculate_damage(self) -> int:
        return self._weapon.damage + self.strength
    
    def attack(self, target: Hero):
        damage = self.calculate_damage()
        print(f"{self._name} slices at {target.get_name()}")
        target.take_damage(damage)

    def __str__(self) -> str:
        """Returns a formatted character sheet for the CLI."""
        return f"""
    ===========================================
                  CHARACTER SHEET
    ===========================================
        Name:           {self._name.upper()}
        Species:        {self._species.name}
        Class:          ROGUE

    HEALTH
        Maximum Health: {self._max_health}
        Current Health: {self.cur_health}

    ATTRIBUTES
        Strength:       {self.strength}
        Intelligence:   {self.intelligence}
        Dexterity:      {self.dexterity}
        Deception:      {self.deception}

    EQUIPMENT
        Weapon:         {self._weapon.display_name}
        Weapon Damage:  {self._weapon.damage}
        Armour:         {self._armour.display_name}
        Armour Defence: {self._armour.defence}

    ===========================================
    """
