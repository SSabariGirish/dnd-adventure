
from enum import Enum


class Weapon(Enum):
    # Knight
    IRON_BROADSWORD = ("Iron Broadsword", 10, "Knight", 100)
    STEEL_LONGSWORD = ("Steel Longsword", 14, "Knight", 250)
    KNIGHTS_GREATSWORD = ("Knight's Greatsword", 18, "Knight", 500)

    # Rogue
    IRON_DAGGER = ("Iron Dagger", 7, "Rogue", 100)
    STEEL_FANG = ("Steel Fang", 10, "Rogue", 240)
    ASSASSINS_BLADE = ("Assassin's Blade", 14, "Rogue", 500)

    # Mage
    APPRENTICE_STAFF = ("Apprentice's Staff", 6, "Mage", 100)
    OAK_STAFF = ("Oak Staff", 9, "Mage", 250)
    ARCANE_SCEPTRE = ("Arcane Sceptre", 13, "Mage", 500)

    def __init__(self, display_name: str, damage: int, hero_class: str, price: str):
        self.display_name = display_name
        self.damage = damage
        self.hero_class = hero_class
        self.price = price
