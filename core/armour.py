
from enum import Enum


class Armour(Enum):
    # Knight
    IRON_CHAINMAIL = ("Iron Chainmail", 4, "Knight")
    STEEL_PLATE = ("Steel Plate", 7, "Knight")
    DRAGONPLATE = ("Dragonplate", 9, "Knight")

    # Rogue
    LEATHER_ARMOUR = ("Leather Armour", 2, "Rogue")
    REINFORCED_LEATHER = ("Reinforced Leather", 3, "Rogue")
    ASSASSIN_GARB = ("Assassin Garb", 5, "Rogue")

    # Mage
    APPRENTICES_ROBES = ("Apprentice's Robes", 1, "Mage")
    ENCHANTED_ROBES = ("Enchanted Robes", 2, "Mage")
    ARCHMAGES_MANTLE = ("Archmage's Mantle", 3, "Mage")

    def __init__(self, display_name: str, defence: int, hero_class: str):
        self.display_name = display_name
        self.defence = defence
        self.hero_class = hero_class
