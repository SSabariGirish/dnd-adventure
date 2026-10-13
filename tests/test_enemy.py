
import unittest

from entities.enemy import Enemy
from entities.knight import Knight
from core.enums import Species
from enemies.templates import spawn_enemy


class TestEnemy(unittest.TestCase):

    def setUp(self):
        self.enemy = Enemy(
            name="Training Gnoll",
            max_health=25,
            damage=8,
            defence=1,
            xp_reward=10,
        )

    def test_initial_health(self):
        self.assertTrue(self.enemy.is_alive())
        self.assertEqual(self.enemy._cur_health, 25)

    def test_take_damage_accounts_for_defence(self):
        self.enemy.take_damage(10)

        self.assertEqual(self.enemy._cur_health, 16)

    def test_damage_cannot_reduce_health_below_zero(self):
        self.enemy.take_damage(1000)

        self.assertEqual(self.enemy._cur_health, 0)
        self.assertFalse(self.enemy.is_alive())

    def test_negative_damage_raises_error(self):
        with self.assertRaises(ValueError):
            self.enemy.take_damage(-1)

    def test_heal(self):
        self.enemy.take_damage(10)
        self.enemy.heal(5)

        self.assertEqual(self.enemy._cur_health, 21)

    def test_healing_cannot_exceed_max_health(self):
        self.enemy.heal(100)

        self.assertEqual(self.enemy._cur_health, 25)

    def test_spawn_enemy_returns_enemy_instance(self):
        enemy = spawn_enemy("wolf")

        self.assertIsInstance(enemy, Enemy)
        self.assertEqual(enemy._name, "Wolf")
        self.assertEqual(enemy._cur_health, 20)

    def test_unknown_enemy_raises_error(self):
        with self.assertRaises(ValueError):
            spawn_enemy("unicorn")

    def test_enemy_attack(self):
        knight = Knight(Species.HUMAN, "Arthur")

        self.enemy.attack(knight)

        self.assertEqual(knight.cur_health, 96)


if __name__ == "__main__":
    unittest.main()
