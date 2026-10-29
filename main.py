import os

from entities.knight import Knight
from entities.mage import Mage
from entities.rogue import Rogue
from entities.hero import Hero
from entities.enemy import Enemy
from core.enums import Species
from utils.display import show_status
from utils.monster_art import ASCII_ART
from adventure.encounters import get_random_encounter, innkeeper_encounter, merchant_encounter, huntsman_encounter, enemy_encounter, peasant_encounter, blacksmith_encounter
from enemies.templates import spawn_enemy

#from google import genai
from dotenv import load_dotenv
from openrouter import OpenRouter

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

visited_places = []

if not api_key:
    raise ValueError("OPENROUTER_API_KEY was not found in .env")

def openrouter_interaction(query: str):
    try:
        with OpenRouter(api_key=api_key) as client:
            response = client.chat.send(
                model="openrouter/free",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are the Dungeon Master of a fantasy "
                            "adventure. Write immersive, original descriptions."
                        )
                    },
                    {
                        "role": "user",
                        "content": query
                    }
                ],
                temperature=0.8,
                max_tokens=200,
                stream=False
            )

            return response.choices[0].message.content

    except Exception as e:
        print(f"\n[Warning] Town generation failed: {e}")
        return None


def generate_town_lore():
    visited = ", ".join(visited_places) if visited_places else "None"

    fallback = (
        "Town: Unknown Village\n"
        "Lore: A quiet settlement stands along the road. "
        "Its weary inhabitants go about their business, "
        "and the village holds secrets yet to be discovered."
    )

    query = f"""
    Generate a new town for a fantasy DnD adventure.

    Previously visited towns: {visited}

    Do not reuse any previously visited town.
    Invent a unique fantasy town name and describe its
    appearance, atmosphere, and one interesting detail.

    Return exactly this format:

    Town: <town name>
    Lore: <town description>
    """

    for _ in range(3):
        response = openrouter_interaction(query)

        if not isinstance(response, str) or not response.strip():
            continue

        town_line = next(
            (
                line.strip()
                for line in response.splitlines()
                if line.strip().lower().startswith("town:")
            ),
            None
        )

        lore_line = next(
            (
                line.strip()
                for line in response.splitlines()
                if line.strip().lower().startswith("lore:")
            ),
            None
        )

        if not town_line or not lore_line:
            continue

        town_name = town_line.split(":", 1)[1].strip()
        lore = lore_line.split(":", 1)[1].strip()

        if not town_name or not lore:
            continue

        if town_name.casefold() in {
            place.casefold() for place in visited_places
        }:
            query += (
                "\nYour previous response reused a town name "
                "or an invalid format. Try a completely different "
                "town and follow the required format exactly."
            )
            continue

        visited_places.append(town_name)

        return f"Town: {town_name}\nLore: {lore}"

    return fallback


def clear_screen():
    input("\nPress Enter to continue...")
    os.system("cls" if os.name == "nt" else "clear")

#Creating the Hero character
def create_hero() -> list:
    info_list = []

    print("===========================================")
    print("          Begin your Adventure!            ")
    print("===========================================")
    name = str(input("What is the name of your Hero?\n"))
    name = name.strip()
    info_list.append(name)
    print("===========================================")
    print(f"Which species does {name} belong to?")
    print("===========================================")
    print("1) HUMAN")
    print("2) ELF")
    print("3) DWARF")
    print("4) DEMON")
    species_choice = int(input("           Choose your species             \n"))

    match species_choice:
        case 1:
            info_list.append(Species.HUMAN)
        case 2:
            info_list.append(Species.ELF)
        case 3:
            info_list.append(Species.DWARF)
        case 4:
            info_list.append(Species.DEMON)
        case _:
            raise ValueError("Invalid Species Chosen")

    print("===========================================")
    print(f"Which class does {name} belong to?")
    print("===========================================")
    print("1) KNIGHT")
    print("2) ROGUE")
    print("3) MAGE") 
    class_choice = int(input("           Choose your class             \n"))

    match class_choice:
        case 1:
            info_list.append("Knight")
        case 2:
            info_list.append("Rogue")
        case 3:
            info_list.append("Mage")
        case _:
            raise ValueError("Invalid Class Chosen")         

    return info_list
    

def handle_encounters(hero: Hero):
    encounter = get_random_encounter(hero)
    print(f'You have encountered {encounter}')
    print(f"Your current Gold: {hero.gold}")
    print(generate_town_lore())

    
    match encounter:
        case "Innkeeper":
            innkeeper_encounter(hero)
        case "Merchant":
            merchant_encounter(hero)
        case "Huntsman":
            huntsman_encounter(hero)
        case "Enemy":
            enemy_encounter(hero)
        case "Peasant":
            peasant_encounter(hero)
        case "Blacksmith":
            blacksmith_encounter(hero)
        case _:
            print(f"{hero.get_name()} avoids the town")
    
    if not hero.is_alive():
        print(f"{hero.get_name()} has courageously fallen in battle and will not be forgotten")
                    

def main():
    invalid = True
    while invalid:
        try:
            choices = create_hero()
            invalid = False
        except ValueError as v:
            print(v)
            clear_screen()

    match choices[2]:
        case 'Knight':
            hero = Knight(choices[1], choices[0])
        case 'Rogue':
            hero = Rogue(choices[1], choices[0])
        case 'Mage':
            hero = Mage(choices[1], choices[0])
    clear_screen()
    print(hero)
    clear_screen()

    while hero.is_alive():
        handle_encounters(hero)
        clear_screen()

if __name__=="__main__":
    main()