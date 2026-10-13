
import unittest
from unittest.mock import patch

from core.enums import Species
from core.weapons import Weapon
from core.armour import Armour
from entities.rogue import Rogue
from entities.enemy import Enemy


class TestRogue(unittest.TestCase):

    def setUp(self):
        self.rogue = Rogue(Species.HUMAN, "Yaevinn")

    def test_initial_health(self):
        self.assertEqual(self.rogue.cur_health, 75)

    def test_class_stats_are_added_to_species_stats(self):
        self.assertEqual(self.rogue.strength, 5)
        self.assertEqual(self.rogue.intelligence, 5)
        self.assertEqual(self.rogue.dexterity, 9)
        self.assertEqual(self.rogue.deception, 7)

    def test_equipment(self):
        self.assertEqual(self.rogue._weapon, Weapon.IRON_DAGGER)
        self.assertEqual(self.rogue._armour, Armour.LEATHER_ARMOUR)

    def test_calculate_damage(self):
        self.assertEqual(self.rogue.calculate_damage(), 12)

    @patch("entities.rogue.random.random", return_value=0.99)
    def test_rogue_takes_damage_when_dodge_fails(self, mock_random):
        self.rogue.take_damage(10)

        self.assertEqual(self.rogue.cur_health, 67)

    @patch("entities.rogue.random.random", return_value=0.10)
    def test_rogue_dodges_attack(self, mock_random):
        self.rogue.take_damage(10)

        self.assertEqual(self.rogue.cur_health, 75)


if __name__ == "__main__":
    unittest.main()
