import random

from dataclasses import dataclass
from entities.enemy import Enemy

@dataclass(frozen=True)
class EnemyTemplate:
    name: str
    max_health: int
    damage: int
    defence: int
    xp_reward: int
    drop_reward: str

ENEMY_TEMPLATES = {

    "goblin": EnemyTemplate(
        name="Goblin",
        max_health=18,
        damage=6,
        defence=0,
        xp_reward=8,
        drop_reward="Goblin Ear"
        ),

    "gnoll": EnemyTemplate(
        name="Gnoll",
        max_health=25,
        damage=8,
        defence=1,
        xp_reward=10,
        drop_reward="Gnoll Fang"
    ),

    "wolf": EnemyTemplate(
        name="Wolf",
        max_health=20,
        damage=7,
        defence=0,
        xp_reward=10,
        drop_reward="Wolf Pelt"
    ),

    "bandit": EnemyTemplate(
        name="Bandit",
        max_health=40,
        damage=12,
        defence=3,
        xp_reward=20,
        drop_reward="Bandit Insignia"
    ),

    "skeleton": EnemyTemplate(
        name="Skeleton",
        max_health=35,
        damage=10,
        defence=2,
        xp_reward=18,
        drop_reward="Bone Fragments"
        ),

    "orc warrior": EnemyTemplate(
        name="Orc Warrior",
        max_health=65,
        damage=15,
        defence=5,
        xp_reward=35,
        drop_reward="Orc Tusk"
        ),

    "dire wolf": EnemyTemplate(
        name="Dire Wolf",
        max_health=55,
        damage=14,
        defence=2,
        xp_reward=35,
        drop_reward="Dire Wolf Pelt"
        ),

    "cultist": EnemyTemplate(
        name="Cultist",
        max_health=45,
        damage=19,
        defence=5,
        xp_reward=40,
        drop_reward="Bloody Robes"
        ),

    "ogre": EnemyTemplate(
        name="Ogre",
        max_health=110,
        damage=20,
        defence=7,
        xp_reward=75,
        drop_reward="Ogre Hide"
        ),

    "wraith": EnemyTemplate(
        name="Wraith",
        max_health=85,
        damage=22,
        defence=5,
        xp_reward=90,
        drop_reward="Wraith Essence"
        ),

    "troll": EnemyTemplate(
        name="Troll",
        max_health=150,
        damage=24,
        defence=8,
        xp_reward=120,
        drop_reward="Troll Tongue"
        ),

    "necromancer": EnemyTemplate(
        name="Necromancer",
        max_health=80,
        damage=28,
        defence=5,
        xp_reward=100,
        drop_reward="Enchanted Grimoire"
    ),

    "wyvern": EnemyTemplate(
        name="Wyvern",
        max_health=200,
        damage=28,
        defence=10,
        xp_reward=250,
        drop_reward="Wyvern Scale"
        ),

    "griffin": EnemyTemplate(
        name="Griffin",
        max_health=250,
        damage=30,
        defence=15,
        xp_reward=500,
        drop_reward="Griffin Feather"
        ),

    "archgriffin": EnemyTemplate(
        name="Archgriffin",
        max_health=450,
        damage=70,
        defence=24,
        xp_reward=1000,
        drop_reward="Archgriffin Talon"
    )
}

SPAWN_WEIGHTS = {
    (1, 2): {
        "goblin": 30,
        "gnoll": 35,
        "wolf": 30,
        "bandit": 2,
        "skeleton" : 2,
        "orc warrior": 0.5,
        "dire wolf": 0.5
    },
    (3, 4): {
        "goblin": 19,
        "gnoll": 22,
        "wolf": 20,
        "bandit": 15,
        "skeleton": 10,
        "orc warrior": 6,
        "dire wolf": 5,
        "cultist": 2,
        "ogre": 1

    },
    (5, 7): {
        "goblin": 8,
        "gnoll": 10,
        "wolf": 8,
        "bandit": 12,
        "skeleton": 12,
        "orc warrior": 8,
        "dire wolf": 8,
        "cultist": 8,
        "ogre": 8,
        "wraith": 8,
        "troll": 5,
        "necromancer": 5
    },
    (8, 10): {
        "goblin": 5,
        "gnoll": 5,
        "wolf": 5,
        "bandit": 7,
        "skeleton": 7,
        "orc warrior": 7,
        "dire wolf": 7,
        "cultist": 7,
        "ogre": 8,
        "wraith": 7,
        "troll": 7,
        "necromancer": 7,
        "wyvern": 8,
        "griffin": 8,
        "archgriffin": 5
    },
    (11, 9999) : {
        "goblin": 2,
        "gnoll": 2,
        "wolf": 2,
        "bandit": 5,
        "skeleton": 5,
        "orc warrior": 5,
        "dire wolf": 5,
        "cultist": 6,
        "ogre": 7,
        "wraith": 7,
        "troll": 7,
        "necromancer": 7,
        "wyvern": 10,
        "griffin": 12,
        "archgriffin": 18
    }
}


BOSS_TEMPLATES = {
    5: EnemyTemplate(
        name="The Goblin King",
        max_health=120,
        damage=16,
        defence=5,
        xp_reward=180,
        drop_reward="Goblin King's Crown"
    ),

    10: EnemyTemplate(
        name="The Undead Champion",
        max_health=220,
        damage=24,
        defence=9,
        xp_reward=300,
        drop_reward="Champion's Blade"
    ),

    15: EnemyTemplate(
        name="The Ogre Warlord",
        max_health=350,
        damage=30,
        defence=12,
        xp_reward=500,
        drop_reward="Warlord's Armour"
    ),

    20: EnemyTemplate(
        name="The Lich Lord",
        max_health=450,
        damage=38,
        defence=15,
        xp_reward=750,
        drop_reward="Lich's Phylactery"
    ),

    25: EnemyTemplate(
        name="The Ancient Wyvern",
        max_health=600,
        damage=45,
        defence=18,
        xp_reward=1000,
        drop_reward="Ancient Wyvern Heart"
    ),

    30: EnemyTemplate(
        name="The Fiend",
        max_health=800,
        damage=55,
        defence=22,
        xp_reward=1500,
        drop_reward="Fiend's Crest"
    ),

    35: EnemyTemplate(
        name="The Ancient Devourer",
        max_health=1200,
        damage=70,
        defence=25,
        xp_reward=0,
        drop_reward=""
    )
}


def get_spawn_weights(level: int) -> dict[str, dict[str, int]]:
    if level <= 2:
        return SPAWN_WEIGHTS[(1, 2)]
    elif level <= 4:
        return SPAWN_WEIGHTS[(3, 4)]
    elif level <= 7:
        return SPAWN_WEIGHTS[(5, 7)]
    elif level <= 10:
        return SPAWN_WEIGHTS[(8, 10)]
    else:
        return SPAWN_WEIGHTS[(11, 9999)]


def spawn_boss(level: int) -> Enemy:
    if level not in BOSS_TEMPLATES:
        raise ValueError(f"No boss exists for level {level}")

    boss = BOSS_TEMPLATES[level]

    print(f"\n{'=' * 45}")
    print(f"A POWERFUL FOE APPROACHES: {boss.name.upper()}!")
    print(f"{'=' * 45}\n")

    return Enemy(
        name=boss.name,
        max_health=boss.max_health,
        damage=boss.damage,
        defence=boss.defence,
        xp_reward=boss.xp_reward,
        drop_reward=boss.drop_reward
    )

def spawn_enemy(level:int) -> Enemy:
    enemy_dict = get_spawn_weights(level)

    enemy_id = random.choices(
        population=list(enemy_dict.keys()),
        weights=list(enemy_dict.values()),
        k=1
    )[0]

    if enemy_id not in ENEMY_TEMPLATES:
        raise ValueError("Enemy not found in Bestiary")

    enemy_template = ENEMY_TEMPLATES[enemy_id]

    return Enemy(
        name=enemy_template.name,
        max_health=enemy_template.max_health,
        damage=enemy_template.damage,
        defence=enemy_template.defence,
        xp_reward=enemy_template.xp_reward,
        drop_reward=enemy_template.drop_reward
    )