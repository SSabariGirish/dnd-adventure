
from enum import Enum


class Weapon(Enum):
    # Knight
    IRON_BROADSWORD = ("Iron Broadsword", 10, "Knight")
    STEEL_LONGSWORD = ("Steel Longsword", 14, "Knight")
    KNIGHTS_GREATSWORD = ("Knight's Greatsword", 18, "Knight")

    # Rogue
    IRON_DAGGER = ("Iron Dagger", 7, "Rogue")
    STEEL_FANG = ("Steel Fang", 10, "Rogue")
    ASSASSINS_BLADE = ("Assassin's Blade", 14, "Rogue")

    # Mage
    APPRENTICE_STAFF = ("Apprentice's Staff", 6, "Mage")
    OAK_STAFF = ("Oak Staff", 9, "Mage")
    ARCANE_SCEPTRE = ("Arcane Sceptre", 13, "Mage")

    def __init__(self, display_name: str, damage: int, hero_class: str):
        self.display_name = display_name
        self.damage = damage
        self.hero_class = hero_class
