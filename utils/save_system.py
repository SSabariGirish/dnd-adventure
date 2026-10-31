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

def save_game(hero):
    save_data = hero_to_dict(hero)

    try:
        json.dumps(save_data)
    except TypeError as e:
        print("JSON serialisation error:", e)
        raise

    with open(SAVE_FILE, "w") as file:
        json.dump(save_data, file, indent=4)

    print("Game saved successfully!")

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

def load_game():
    try:
        with open(SAVE_FILE, "r") as file:
            save_data = json.load(file)

    except FileNotFoundError:
        print("No save file found.")
        return None

    character = save_data["character"]
    stats = save_data["stats"]
    equipment = save_data["equipment"]

    hero_classes = {
        "Knight": Knight,
        "Mage": Mage,
        "Rogue": Rogue
    }

    hero_class = hero_classes[character["class"]]
    species = Species[character["species"]]

    hero = hero_class(species, character["name"])

    hero.level = character["level"]
    hero.xp = character["xp"]
    hero.gold = character["gold"]

    hero.cur_health = stats["health"]
    hero._max_health = stats["max_health"]
    hero.cur_mana = stats["mana"]
    hero._max_mana = stats["max_mana"]

    hero.strength = stats["strength"]
    hero.intelligence = stats["intelligence"]
    hero.dexterity = stats["dexterity"]
    hero.deception = stats["deception"]

    hero._weapon = Weapon[equipment["weapon"]]
    hero._armour = Armour[equipment["armour"]]

    inventory = save_data["inventory"]

    hero.healing_potion_inventory = inventory["healing_potions"]
    hero.mana_potion_inventory = inventory["mana_potions"]
    hero.junk_inventory = inventory["junk"]

    hero.quests = []

    for quest_data in save_data["quests"]:
        quest = PeasantQuest(
            quest_data["monster_name"],
            quest_data["required_kills"],
            quest_data["xp_reward"],
            quest_data["gold_reward"]
        )

        quest.current_kills = quest_data["current_kills"]
        quest.completed = quest_data["completed"]

        hero.quests.append(quest)

    game_state = save_data["game_state"]
    hero.game_completed = game_state["game_completed"]
    hero.bosses_faced = game_state["bosses_faced"]

    class_state = save_data.get("class_state", {})

    if isinstance(hero, Knight):
        hero._shield_active = class_state.get("shield_active", False)

    elif isinstance(hero, Rogue):
        hero._stance = class_state.get("stance", "MELEE")
        hero._evasion = class_state.get("evasion", 0.25)

    print(f"\nWelcome back, {hero.get_name()}!")

    return hero