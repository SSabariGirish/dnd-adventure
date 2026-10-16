from .hero import Hero

class Enemy(Hero):

    def __init__(self, name: str, max_health: int, damage: int, defence: int, xp_reward: int, drop_reward: str):
        self._name = name
        self._max_health = max_health
        self._cur_health = max_health
        self._damage = damage
        self._defence = defence
        self._xp_reward = xp_reward
        self._drop_reward = drop_reward

    def take_damage(self, damage: int):
        if damage < 0:
            raise ValueError("Damage should not be negative")

        actual_damage = max(
            0, 
            damage - self._defence
        )

        self._cur_health = max(
            0, 
            self._cur_health - actual_damage
        )

        print(f"{self._name} has taken {actual_damage} damage")

    def heal(self, heal_amt: int):
        if heal_amt < 0:
            raise ValueError("Healing amount should not be negative")

        self._cur_health = min(
            self._max_health, 
            self._cur_health + heal_amt
        )

    def is_alive(self) -> bool:
        return self._cur_health > 0

    def get_xp_reward(self) -> int:
        return self._xp_reward

    def get_drop_reward(self) -> str:
        return self._drop_reward

    def attack(self, target: Hero):
        print(f"{self._name} has mauled {target.get_name()}")
        target.take_damage(self._damage)
    