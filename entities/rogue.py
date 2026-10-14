from .hero import Hero
from core.enums import Species
from core.weapons import Weapon
from core.armour import Armour
import random

class Rogue(Hero):

    def __init__(self, species: Species, name: str):
        super().__init__(species, name, Weapon.IRON_DAGGER, Armour.LEATHER_ARMOUR, 75)
        self._evasion = 0.20
        self.set_stats()
    
    def set_stats(self):
        self.cur_health = self._max_health
        self.strength += 3
        self.intelligence += 4
        self.dexterity += 8
        self.deception += 5
        self.max_mana = 20 + (self.intelligence * 2)
        self.cur_mana = self.max_mana

    def raise_evasion(self):
        mana_cost = 10
        if self.cur_mana < mana_cost:
                print('Not enough mana to raise evasion')
                return
        
        self.cur_mana -= mana_cost
        self._evasion = 0.40

        print(f"{self._name} has become more nimble")
        
    def take_damage(self, damage: int):
        
        if random.random() <= self._evasion:
            print(f"{self._name} dodged the attack!")
        else:
            damage = max(0, damage - self._armour.defence)
            super().take_damage(damage)

    def calculate_damage(self) -> int:
        return self._weapon.damage + self.strength
    
    def attack(self, target: Hero):
        self._evasion = 0.20
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

    HEALTH & MANA
        Maximum Health: {self._max_health}
        Current Health: {self.cur_health}
        Maximum Mana:   {self.max_mana}
        Current Mana:   {self.cur_mana}

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
