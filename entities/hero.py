import os
import math

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
        self._max_mana = 0
        self.cur_mana = 0
        self.healing_potion_inventory = ['Minor Healing Draught', 'Minor Healing Draught']
        self.mana_potion_inventory = ['Minor Arcane Elixir', 'Minor Arcane Elixir']

        #Base stats
        self.strength = species.strength
        self.intelligence = species.intelligence
        self.dexterity = species.dexterity
        self.deception = species.deception
        self.cur_health = 0
        self.level = 1
        self.xp = 0
                        

    def set_stats(self):
        """A method that would be inherited by child classes to update stats based on their class"""
        pass

    def take_damage(self, damage: int) -> None:
        """Reduces cur_health by amount, capped at 0."""
        if damage < 0:
            raise ValueError("Invalid damage amount")
        self.cur_health -= damage
        self.cur_health = max(0, self.cur_health)
        print(f"{self._name} has taken {damage} damage")

    def heal(self, heal_amt: int) -> None:
        if heal_amt <= 0:
            raise ValueError("Invalid heal amount")
        
        self.cur_health += heal_amt
        self.cur_health = min(self._max_health, self.cur_health)

    def restore_mana(self, mana_amt: int) -> None:
        if mana_amt < 0:
            raise ValueError("invalid mana restoration amount")

        self.cur_mana += mana_amt
        self.cur_mana = min(self.cur_mana, self._max_mana)

    def get_next_level_xp(self, level: int) -> int:
        return math.floor(100 * (level ** 1.5))

    def verify_level_up(self):
        cumulative_xp =  self.get_next_level_xp(self.level)
        while self.xp > cumulative_xp:
            print("LEVEL UP!!!")
            self.level += 1
            cumulative_xp =  self.get_next_level_xp(self.level)

    def consume_healing_potion(self) -> bool:
        if len(self.healing_potion_inventory) == 0:
            print("No healing potions available in the inventory")
            return False

        while True:
            print("===========================================")
            print("         Healing Potion Inventory          ")
            print("===========================================")

            print("0) Go Back")
            for i, potion in enumerate(self.healing_potion_inventory):
                print(f"{i + 1}) {potion}")

            try:
                choice = int(input("         Choose Healing Potion          "))
                if choice == 0:
                    return False
                
                choice -= 1
                

                if choice not in range(len(self.healing_potion_inventory)):
                    input("\nPress Enter to continue...")
                    os.system("cls" if os.name == "nt" else "clear")
                    print("Selected option is not in range of healing potion inventory\n\n")
                    continue

                match self.healing_potion_inventory[choice]:
                    case "Minor Healing Draught":
                        self.heal(15)
                    case "Concentrated Healing Draught":
                        self.heal(45)
                    case "Pure Vitality Draught":
                        self.heal(self._max_health)

                self.healing_potion_inventory.pop(choice)
                return True

            except ValueError:
                print("Please enter a valid number.")


    def consume_mana_potion(self) -> bool:
        if len(self.mana_potion_inventory) == 0:
            print("No mana potions available in the inventory")
            return False

        while True:
            print("===========================================")
            print("           Mana Potion Inventory           ")
            print("===========================================")

            print("0) Go Back")
            for i, potion in enumerate(self.mana_potion_inventory):
                print(f"{i + 1}) {potion}")

            try:
                choice = int(input("           Choose Mana Potion           "))
                if choice == 0:
                    return False
                
                choice -= 1

                if choice not in range(len(self.mana_potion_inventory)):
                    input("\nPress Enter to continue...")
                    os.system("cls" if os.name == "nt" else "clear")
                    
                    print("Selected option is not in range of mana potion inventory\n\n")

                    continue

                match self.mana_potion_inventory[choice]:
                    case "Minor Arcane Elixir":
                        self.restore_mana(15)
                    case "Potent Leyline Flask":
                        self.restore_mana(45)
                    case "Supreme Celestial Nectar":
                        self.restore_mana(self._max_mana)

                self.mana_potion_inventory.pop(choice)
                return True

            except ValueError:
                print("Please enter a valid number.")        

    def is_alive(self) -> bool:
        return self.cur_health > 0

    def get_name(self) -> str:
        return self._name

    def get_max_mana(self) -> int:
        return self._max_mana

    def get_max_health(self) -> int:
        return self._max_health

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

    