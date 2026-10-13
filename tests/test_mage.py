
import unittest

from core.enums import Species
from core.weapons import Weapon
from core.armour import Armour
from entities.mage import Mage
from entities.enemy import Enemy


class TestMage(unittest.TestCase):

    def setUp(self):
        self.mage = Mage(Species.HUMAN, "Triss Merigold of Maribor")

    def test_initial_health(self):
        self.assertEqual(self.mage.cur_health, 50)

    def test_class_stats_are_added_to_species_stats(self):
        self.assertEqual(self.mage.strength, 4)
        self.assertEqual(self.mage.intelligence, 11)
        self.assertEqual(self.mage.dexterity, 5)
        self.assertEqual(self.mage.deception, 6)

    def test_equipment(self):
        self.assertEqual(self.mage._weapon, Weapon.APPRENTICE_STAFF)
        self.assertEqual(self.mage._armour, Armour.APPRENTICES_ROBES)

    def test_mana_initialisation(self):
        self.assertEqual(self.mage.max_mana, 52)
        self.assertEqual(self.mage.cur_mana, 52)

    def test_calculate_damage(self):
        self.assertEqual(self.mage.calculate_damage(), 17)

    def test_cast_spell(self):
        enemy = Enemy("Training Dummy", 100, 1, 0, 0)

        self.mage.cast_spell(enemy)

        self.assertEqual(enemy._cur_health, 72)
        self.assertEqual(self.mage.cur_mana, 42)

    def test_spell_fails_without_enough_mana(self):
        enemy = Enemy("Training Dummy", 100, 1, 0, 0)
        self.mage.cur_mana = 5

        self.mage.cast_spell(enemy)

        self.assertEqual(enemy._cur_health, 100)
        self.assertEqual(self.mage.cur_mana, 5)


if __name__ == "__main__":
    unittest.main()
