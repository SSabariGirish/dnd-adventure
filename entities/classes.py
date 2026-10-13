from hero import Hero
from core.enums import Species
from core.weapons import Weapon
from core.armour import Armour

import random

class Knight(Hero):

    def __init__(self, species: Species, name: str):
        super().__init__(species, name, Weapon.IRON_BROADSWORD, Armour.IRON_CHAINMAIL, 100)
        self.shield_block = False
        self.set_stats()

    def set_stats(self):
        self.cur_health = self._max_health
        self.strength += 8
        self.intelligence += 3
        self.dexterity += 5
        self.deception += 4
        

    def take_damage(self, damage: int):
        if self.shield_block:
            damage = damage // 2
            self.shield_block = False
        
        damage = max(0, damage - self._armour.defence)
        super().take_damage(damage)

    def calculate_damage(self) -> int:
        return self._weapon.damage + self.strength

    def attack(self, target: Hero):
        self.shield_block = False
        damage = self.calculate_damage()
        target.take_damage(damage)
        print(f"{self._name} uses {self._weapon.display_name} and attacks for {damage} damage")

    def raise_shield(self):
        self.shield_block = True
        print(f"{self.name} raises their shield!")


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
            return

        damage = max(0, damage - self._armour.defence)
        super().take_damage(damage)

    def calculate_damage(self) -> int:
        return self._weapon.damage + self.strength
    
    def attack(self, target: Hero):
        damage = self.calculate_damage()
        target.take_damage(damage)



class Mage(Hero):

    def __init__(self, species: Species, name: str):
        super().__init__(species, name, Weapon.APPRENTICE_STAFF, Armour.APPRENTICES_ROBES, 50)
        self.cur_mana = 0
        self.max_mana = 0
        self.set_stats()
        
    def set_stats(self):
        self.cur_health = self._max_health
        self.strength += 2
        self.intelligence += 10
        self.dexterity += 4
        self.deception += 4
        self.max_mana = 30 + (self.intelligence * 2)
        self.cur_mana = self.max_mana
            

    def take_damage(self, damage: int):
            damage = max(0, damage - self._armour.defence)
            super().take_damage(damage)

    def calculate_damage(self) -> int:
        return self._weapon.damage + self.intelligence
    
    def attack(self, target: Hero):
        damage = self.calculate_damage()
        target.take_damage(damage)

    def cast_spell(self, target: Hero):
        mana_cost = 10

        if self.cur_mana < mana_cost:
            print('Not enough mana to cast a spell')
            return

        self.cur_mana -= mana_cost

        damage = self._weapon.damage + (self.intelligence * 2)
        target.take_damage(damage)

        print(f"{self._name} casts Arcane bolt for {damage} damage")