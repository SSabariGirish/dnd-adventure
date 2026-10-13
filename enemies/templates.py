from dataclasses import dataclass
from entities.enemy import Enemy

@dataclass(frozen=True)
class EnemyTemplate:
    name: str
    max_health: int
    damage: int
    defence: int
    xp_reward: int

ENEMY_TEMPLATES = {

    "gnoll": EnemyTemplate(
        name="Gnoll",
        max_health=25,
        damage=8,
        defence=1,
        xp_reward=10,
    ),

    "wolf": EnemyTemplate(
        name="Wolf",
        max_health=20,
        damage=7,
        defence=0,
        xp_reward=10,
    ),

    "undead": EnemyTemplate(
        name="Undead",
        max_health=50,
        damage=14,
        defence=4,
        xp_reward=25,
    ),

    "bandit": EnemyTemplate(
        name="Bandit",
        max_health=40,
        damage=12,
        defence=3,
        xp_reward=20,
    ),

    "necromancer": EnemyTemplate(
        name="Necromancer",
        max_health=80,
        damage=18,
        defence=3,
        xp_reward=60,
    ),

    "dragon": EnemyTemplate(
        name="Dragon",
        max_health=250,
        damage=30,
        defence=15,
        xp_reward=1000
    )
}

def spawn_enemy(enemy_id: str) -> Enemy:
    if enemy_id not in ENEMY_TEMPLATES:
        raise ValueError("Enemy not found in Bestiary")

    enemy_template = ENEMY_TEMPLATES[enemy_id]

    return Enemy(
        name=enemy_template.name,
        max_health=enemy_template.max_health,
        damage=enemy_template.damage,
        defence=enemy_template.defence,
        xp_reward=enemy_template.xp_reward
    )