
import unittest

from core.enums import Species
from core.weapons import Weapon
from core.armour import Armour
from entities.knight import Knight
from entities.enemy import Enemy


class TestKnight(unittest.TestCase):

    def setUp(self):
        self.knight = Knight(Species.HUMAN, "Siegfried")

    def test_equipment(self):
        self.assertEqual(self.knight._weapon, Weapon.IRON_BROADSWORD)
        self.assertEqual(self.knight._armour, Armour.IRON_CHAINMAIL)

    def test_class_stats_are_added_to_species_stats(self):
        self.assertEqual(self.knight.strength, 10)
        self.assertEqual(self.knight.intelligence, 4)
        self.assertEqual(self.knight.dexterity, 6)
        self.assertEqual(self.knight.deception, 6)

    def test_calculate_damage(self):
        self.assertEqual(self.knight.calculate_damage(), 20)

    def test_shield_halves_incoming_damage(self):
        self.knight.raise_shield()
        self.knight.take_damage(20)

        self.assertEqual(self.knight.cur_health, 94)

    def test_shield_only_blocks_one_hit(self):
        self.knight.raise_shield()
        self.knight.take_damage(20)
        self.knight.take_damage(20)
        
        self.assertEqual(self.knight.cur_health, 88)

    def test_attacking_drops_shield(self):
        enemy = Enemy("Training Dummy", 100, 1, 0, 0)

        self.knight.raise_shield()
        self.knight.attack(enemy)
        self.knight.take_damage(20)

        self.assertEqual(self.knight.cur_health, 84)


if __name__ == "__main__":
    unittest.main()
