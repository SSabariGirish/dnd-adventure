from .hero import Hero
from core.enums import Species
from core.weapons import Weapon
from core.armour import Armour

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
        print(f"{self._name} swings at {target.get_name()} for {damage} damage")

    def cast_spell(self, target: Hero):
        mana_cost = 10

        if self.cur_mana < mana_cost:
            print('Not enough mana to cast a spell')
            return

        self.cur_mana -= mana_cost

        damage = self._weapon.damage + (self.intelligence * 2)
        target.take_damage(damage)

        print(f"{self._name} casts Arcane bolt for {damage} damage")

    def __str__(self) -> str:
        """Returns a formatted character sheet for the CLI."""
        return f"""
        ===========================================
                      CHARACTER SHEET
        ===========================================
            Name:           {self._name.upper()}
            Species:        {self._species.name}
            Class:          MAGE
    
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