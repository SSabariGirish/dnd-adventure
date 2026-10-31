from .hero import Hero
from core.enums import Species
from core.weapons import Weapon
from core.armour import Armour
import random

class Rogue(Hero):

    def __init__(self, species: Species, name: str):
        super().__init__(species, name, Weapon.IRON_DAGGER, Armour.LEATHER_ARMOUR, 85)
        self._evasion = 0.25
        self._stance = "MELEE"
        self.set_stats()
    
    def set_stats(self):
        self.cur_health = self._max_health
        self.strength += 4
        self.intelligence += 4
        self.dexterity += 10
        self.deception += 5
        self._max_mana = 20 + (self.intelligence * 2)
        self.cur_mana = self._max_mana

    def get_stance(self) -> str:
        return self._stance

    def raise_evasion(self) -> bool:
        mana_cost = 10
        if self.cur_mana < mana_cost:
                print('Not enough mana to raise evasion')
                print('Spell failed')
                return False
        
        self.cur_mana -= mana_cost
        if self._stance == "MELEE":
            self._evasion = 0.40
        else:
            self._evasion = 0.65

        print(f"{self._name} has become more nimble")
        return True
        
    def take_damage(self, damage: int):
        
        if random.random() <= self._evasion:
            print(f"{self._name} dodged the attack!")
        else:
            damage = max(0, damage - self._armour.defence)
            super().take_damage(damage)

    def calculate_damage(self) -> int:
        if self._stance == 'MELEE':
            return self._weapon.damage + self.strength
        else:
            return (self._weapon.damage // 4) + self.dexterity

    def switch_stance(self) -> bool:
        if self._stance == "MELEE":
            self._stance = "RANGED"
            if self._evasion == 0.45:
                self._evasion = 0.65
            else:
                self._evasion = 0.40 # From 25%, it is increased to 40%
        else:
            self._stance = "MELEE"
            if self._evasion == 0.65:
                self._evasion = 0.45
            else:
                self._evasion = 0.25 #From 40%, down to 25%
        return True
            
    
    def attack(self, target: Hero):
        if self._stance == "MELEE":
            self._evasion = 0.25
        else:
            self._evasion = 0.40

        damage = self.calculate_damage() * self.attack_modifier

        print(f"{self._name} slices at {target.get_name()}")
        target.take_damage(damage)

        self.attack_modifier = 1.0
        return True

    def verify_level_up(self):
        old_level = self.level
        level_up = super().verify_level_up()
        
        if level_up:
            levels_gained = self.level - old_level

            self._max_health += 8 * levels_gained
            self.cur_health = self._max_health
            self._max_mana += 8 * levels_gained
            self.cur_mana = self._max_mana
            self.strength += levels_gained
            self.dexterity += 3 * levels_gained
            self.deception += 2 * levels_gained
    
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
        Maximum Mana:   {self._max_mana}
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
