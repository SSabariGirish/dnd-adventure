
from enum import Enum


class Armour(Enum):
    # Knight
    IRON_CHAINMAIL = ("Iron Chainmail", 4, "Knight", 100)
    STEEL_PLATE = ("Steel Plate", 7, "Knight", 250)
    DRAGONPLATE = ("Dragonplate", 9, "Knight", 500)

    # Rogue
    LEATHER_ARMOUR = ("Leather Armour", 2, "Rogue", 100)
    REINFORCED_LEATHER = ("Reinforced Leather", 3, "Rogue", 250)
    ASSASSIN_GARB = ("Assassin Garb", 5, "Rogue", 500)

    # Mage
    APPRENTICES_ROBES = ("Apprentice's Robes", 1, "Mage", 100)
    ENCHANTED_ROBES = ("Enchanted Robes", 2, "Mage", 250)
    ARCHMAGES_MANTLE = ("Archmage's Mantle", 3, "Mage", 500)

    def __init__(self, display_name: str, defence: int, hero_class: str, armour_cost: int):
        self.display_name = display_name
        self.defence = defence
        self.hero_class = hero_class
        self.armour_cost = armour_cost
