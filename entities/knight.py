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
        self._max_mana = 10 + (self.intelligence * 2)
        self.cur_mana = self._max_mana
        

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
        print(f"{self._name} swings at {target.get_name()}")
        target.take_damage(damage)
        self.attack_modifier = 1.0
        return True

    def raise_shield(self) -> bool:
        mana_cost = 10
        
        if self.cur_mana < mana_cost:
                print('Not enough mana to raise holy shield')
                print('Spell failed')
                return False
        
        self.cur_mana -= mana_cost
                
        self.shield_block = True
        print(f"{self._name} raises their shield!")
        return True

    def verify_level_up(self):
        level_up = super().verify_level_up()
        if level_up:
            self._max_health += 12
            self.cur_health = self._max_health
            self._max_mana += 3
            self.cur_mana = self._max_mana
            self.strength += 2
            self.dexterity += 1

    def __str__(self) -> str:
        """Returns a formatted character sheet for the CLI."""
        return f"""
    ===========================================
                  CHARACTER SHEET
    ===========================================
        Name:           {self._name.upper()}
        Species:        {self._species.name}
        Class:          KNIGHT

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