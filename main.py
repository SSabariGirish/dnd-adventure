import os

from entities.knight import Knight
from entities.mage import Mage
from entities.rogue import Rogue
from entities.hero import Hero
from entities.enemy import Enemy
from core.enums import Species
from utils.display import show_status
from utils.monster_art import ASCII_ART
from adventure.encounters import get_random_encounter, innkeeper_encounter, merchant_encounter, huntsman_encounter, enemy_encounter
from enemies.templates import spawn_enemy

from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=GOOGLE_API_KEY)


def gemini_interaction(query: str) -> str:
    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=query
    )
    return interaction.output_text

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
    match encounter:
        case "Innkeeper":
            innkeeper_encounter(hero)
        case "Merchant":
            merchant_encounter(hero)
        case "Huntsman":
            huntsman_encounter(hero)
        case "Enemy":
            enemy_encounter(hero)
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