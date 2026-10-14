import os

from entities.knight import Knight
from entities.mage import Mage
from entities.rogue import Rogue
from entities.hero import Hero
from entities.enemy import Enemy
from core.enums import Species

from enemies.templates import spawn_enemy

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

def get_player_action(hero: Knight | Mage | Rogue) -> int:
    print("===========================================")
    print("         What are you Going to Do?         ")
    print("===========================================")
    print("1) ATTACK")
    if isinstance(hero, Knight):
        print("2) RAISE SHIELD")
    elif isinstance(hero, Mage):
        print("2) CAST SPELL")

    choice = int(input("Choose your action\n"))

    match choice:
        case 1 | 2:
            return choice
        case _:
            raise ValueError("Invalid Option")

def combat(hero: Knight | Mage | Rogue, enemy: Enemy):
    print(hero)
    action_choice = get_player_action(hero)
    
    match action_choice:
        case 1:
            hero.attack(enemy)
        case 2:
            if isinstance(hero, Knight):
                hero.raise_shield()
            elif isinstance(hero, Mage):
                hero.cast_spell(enemy)
    
    enemy.attack(hero)
    clear_screen()


def main():
    choices = create_hero()

    match choices[2]:
        case 'Knight':
            hero = Knight(choices[1], choices[0])
        case 'Rogue':
            hero = Rogue(choices[1], choices[0])
        case 'Mage':
            hero = Mage(choices[1], choices[0])
    print(hero)

    while hero.is_alive():
        cur_enemy = spawn_enemy('gnoll')
        combat(hero, cur_enemy)
        
        if not cur_enemy.is_alive():
            print(f"{hero.get_name()} has slain {cur_enemy.get_name()}")

        if not hero.is_alive():
            print(f"{hero.get_name()} has courageously fallen in battle and will not be forgotten")

if __name__=="__main__":
    main()