from .hero import Hero
from core.enums import Species
from core.weapons import Weapon
from core.armour import Armour

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
        print(f"{self._name} raises their shield!")

    def __str__(self) -> str:
        """Returns a formatted character sheet for the CLI."""
        return f"""
    ===========================================
                CHARACTER SHEET
    ===========================================
        Name:           {self._name.upper()}
        Species:        {self._species.name}
        Class:          KNIGHT

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