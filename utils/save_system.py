import json

from entities.hero import Hero
from entities.knight import Knight
from entities.mage import Mage
from entities.rogue import Rogue

from core.enums import Species
from core.weapons import Weapon
from core.armour import Armour

from adventure.quest import PeasantQuest

SAVE_FILE = "save.json"

def save_game(save_data: dict):
    with open(SAVE_FILE, "w") as file:
        json.dump(save_data, file, indent=4)

    print("Game Saved Successfully!")

def hero_to_dict(hero: Hero) -> dict:
    save_data = {
        "save_version": 1,

        "character": {
            "name": hero.get_name(),
            "class": hero.__class__.__name__,
            "species": hero._species.name,
            "level": hero.level,
            "xp": hero.xp,
            "gold": hero.gold
        },

        "stats": {
            "health": hero.cur_health,
            "max_health": hero.get_max_health(),
            "mana": hero.cur_mana,
            "max_mana": hero.get_max_mana(),
            "strength": hero.strength,
            "intelligence": hero.intelligence,
            "dexterity": hero.dexterity,
            "deception": hero.deception
        },

        "equipment": {
            "weapon": hero._weapon.name,
            "armour": hero._armour.name
        },

        "inventory": {
            "healing_potions": hero.healing_potion_inventory,
            "mana_potions": hero.mana_potion_inventory,
            "junk": hero.junk_inventory
        },

        "quests": [
            {
                "monster_name": quest.monster_name,
                "required_kills": quest.required_kills,
                "current_kills": quest.current_kills,
                "xp_reward": quest.xp_reward,
                "gold_reward": quest.gold_reward,
                "completed": quest.completed
            }
            for quest in hero.quests
        ],

        "game_state": {
            "game_completed": hero.game_completed,
            "bosses_faced": hero.bosses_faced
        }

    }

    if isinstance(hero, Knight):
        save_data["class_state"] = {
            "shield_block": hero.shield_block
        }

    elif isinstance(hero, Rogue):
        save_data["class_state"] = {
            "stance": hero._stance,
            "evasion": hero._evasion
        }

    return save_data